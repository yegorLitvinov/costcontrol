from django.db.models import Sum, functions
from django.db.models.functions import ExtractMonth, ExtractYear
from django.utils import timezone
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from apps.core.views import OwnerMixin

from .filters import BalanceRecordYearFilter, CategoryMonthOfYearFilter
from .models import BalanceRecord, Category
from .serializers import (
    BalanceRecordSerializer,
    CategorySerializer,
    CategoryStatisticsSerializer,
    YearStatisticsSerializer,
)
from .utils import fill_empty_period, generate_filled_monthes


class CategoryStatisticsListView(OwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [CategoryMonthOfYearFilter]
    filterset_fields = ["kind"]
    queryset = Category.objects.all()
    serializer_class = CategoryStatisticsSerializer

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.annotate(total=Sum("balance_records__amount"))


class YearStatisticsListView(OwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [BalanceRecordYearFilter]
    queryset = BalanceRecord.objects.all()
    serializer_class = YearStatisticsSerializer

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        qs = (
            qs.annotate(month=functions.ExtractMonth("created_at"))
            .only("category__kind", "amount", "month")
            .values("category__kind", "month")
            .annotate(total=Sum("amount"))
            .order_by("month", "category__kind")
        )
        return qs


class HistoryView(OwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [SearchFilter]
    queryset = BalanceRecord.objects.order_by("-created_at")
    serializer_class = BalanceRecordSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ["category"]
    search_fields = ["comment"]


class TotalView(APIView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        def get_amount(qs):
            values = qs.annotate(total=Sum("amount")).values_list("total", flat=True)
            return sum(values)

        records = BalanceRecord.objects.filter(category__user=request.user)
        spendings = records.filter(category__kind=Category.KIND_SPENDING)
        proceeds = records.filter(category__kind=Category.KIND_PROCEED)
        spendings_amount = get_amount(spendings)
        proceeds_amount = get_amount(proceeds)
        return Response({"accumulated": proceeds_amount - spendings_amount})


class FilledMonthesView(APIView):
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        filled_months = generate_filled_monthes(request.user.date_joined, timezone.now())
        return Response(filled_months)


class CategoryViewSet(OwnerMixin, viewsets.ModelViewSet):
    filterset_fields = ["kind"]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(methods=["get"], detail=True)
    def year_statistics(self, request, pk):
        date_joined = request.user.date_joined
        now = timezone.now()
        category = self.get_object()
        records = list(
            category.balance_records.annotate(
                year=ExtractYear("created_at"), month=ExtractMonth("created_at")
            )
            .only("amount", "year", "month")
            .values("year", "month")
            .annotate(total=Sum("amount"))
            .order_by("year", "month")
        )
        records = fill_empty_period(records, date_joined, now)
        return Response(records)


class BalanceRecordViewSet(OwnerMixin, viewsets.ModelViewSet):
    serializer_class = BalanceRecordSerializer
    queryset = BalanceRecord.objects.all()

from django.db.models import Sum, functions
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from apps.core.view_mixins import OwnerMixin

from .filters import BalanceRecordYearFilter, CategoryMonthOfYearFilter
from .models import BalanceRecord, Category
from .permissions import IsCategoryOwner, IsRecordOwner
from .serializers import (
    BalanceRecordSerializer,
    CategorySerializer,
    CategoryStatisticsSerializer,
    YearStatisticsSerializer,
)
from .utils import FilledMonthesCache
from .view_mixins import BalanceRecordOwnerMixin


class CategoryStatisticsListView(OwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [CategoryMonthOfYearFilter]
    filter_fields = ["kind"]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryStatisticsSerializer

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.annotate(total=Sum("balance_records__amount"))


class YearStatisticsListView(BalanceRecordOwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [BalanceRecordYearFilter]
    permission_classes = [IsAuthenticated]
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


class HistoryView(BalanceRecordOwnerMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BalanceRecord.objects.order_by("-created_at")
    serializer_class = BalanceRecordSerializer
    pagination_class = PageNumberPagination


class FilledMonthesView(APIView):
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        filled_months = FilledMonthesCache(request.user).get_filled_months()
        return JsonResponse(filled_months)


class CategoryViewSet(OwnerMixin, viewsets.ModelViewSet):
    filter_fields = ["kind"]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsCategoryOwner]

    @action(methods=["get"], detail=True)
    def year_statistics(self, request, pk):
        category = self.get_object()
        year_filter = BalanceRecordYearFilter()
        records = year_filter.filter_queryset(request, category.balance_records, self)
        records = (
            records.annotate(month=functions.ExtractMonth("created_at"))
            .only("amount", "month")
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )
        return JsonResponse(list(records), safe=False)


class BalanceRecordViewSet(BalanceRecordOwnerMixin, viewsets.ModelViewSet):
    serializer_class = BalanceRecordSerializer
    queryset = BalanceRecord.objects.all()
    permission_classes = [IsRecordOwner]

from django.db.models import Sum
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from apps.core.view_mixins import OwnerMixin

from .filters import MonthOfYearFilter
from .models import BalanceRecord, Category
from .serializers import BalanceRecordSerializer, CategoryStatisticSerializer
from .utils import FilledMonthesCache


class CategoryStatisticListView(OwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [MonthOfYearFilter]
    filter_fields = ['kind']
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryStatisticSerializer

    def filter_queryset(self, queryset):
        statistics = super().filter_queryset(queryset)
        return statistics.annotate(
            total=Sum('balance_records__amount')
        )


class HistoryView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BalanceRecord.objects.all()
    serializer_class = BalanceRecordSerializer

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        qs = qs.filter(category__user=self.request.user).order_by('-created_at')[:20]
        return qs


class FilledMonthesView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        filled_monthes = FilledMonthesCache(request.user).get_filled_monthes()
        return JsonResponse(filled_monthes, safe=False)

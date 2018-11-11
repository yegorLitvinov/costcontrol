from calendar import monthrange

from django.utils import timezone
from django_filters.filters import Filter

from .serializers import MonthOfYearSerializer, YearSerializer


class CategoryMonthOfYearFilter(Filter):
    def filter_queryset(self, request, queryset, view):
        serializer = MonthOfYearSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        month = serializer.validated_data.get("month")
        year = serializer.validated_data.get("year")
        start_date = timezone.datetime(
            year, month, 1, tzinfo=timezone.get_current_timezone()
        )
        end_day = monthrange(year, month)[1]
        end_date = timezone.datetime(
            year, month, end_day, 23, 59, 59, tzinfo=timezone.get_current_timezone()
        )
        qs = queryset.filter(
            balance_records__created_at__range=(start_date, end_date)
        ).distinct()
        return qs


class BalanceRecordYearFilter(Filter):
    def filter_queryset(self, request, queryset, view):
        serializer = YearSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        year = serializer.validated_data["year"]
        return queryset.filter(created_at__year=year)

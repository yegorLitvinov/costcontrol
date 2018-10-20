from calendar import monthrange

from django.utils import timezone
from django_filters.filters import Filter

from .forms import DateFilterForm, YearFilterForm


class CategoryMonthOfYearFilter(Filter):
    def filter_queryset(self, request, queryset, view):
        form = DateFilterForm(request.GET)
        if form.is_valid():
            month = form.cleaned_data.get("month")
            year = form.cleaned_data.get("year")
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
        # TODO: rise validation error.
        return queryset.none()


class BalanceRecordYearFilter(Filter):
    def filter_queryset(self, request, queryset, view):
        form = YearFilterForm(request.GET)
        if form.is_valid():
            year = form.cleaned_data["year"]
            return queryset.filter(created_at__year=year)
        return queryset.none()

from django_filters.filters import Filter

from .forms import DateFilterForm, YearFilterForm


class CategoryMonthOfYearFilter(Filter):
    def filter_queryset(self, request, queryset, view):
        form = DateFilterForm(request.GET)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            return (
                queryset
                .filter(balance_records__created_at__month=month)
                .filter(balance_records__created_at__year=year)
            )
        return queryset.none()


class BalanceRecordYearFilter(Filter):
    def filter_queryset(self, request, queryset, view):
        form = YearFilterForm(request.GET)
        if form.is_valid():
            year = form.cleaned_data['year']
            return queryset.filter(created_at__year=year)
        return queryset.none()

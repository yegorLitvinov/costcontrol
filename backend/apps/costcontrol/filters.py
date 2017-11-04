from django_filters.filters import Filter

from .forms import DateFilterForm


class MonthOfYearFilter(Filter):
    balances_field = ''

    def filter_queryset(self, request, queryset, view):
        form = DateFilterForm(request.GET)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            qs_filter = {}
            if month:
                qs_filter['balance_records__created_at__month'] = month
            if year:
                qs_filter['balance_records__created_at__year'] = year
            return queryset.filter(**qs_filter)
        return queryset.none()

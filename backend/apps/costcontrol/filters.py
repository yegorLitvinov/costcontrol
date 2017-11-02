from django_filters.filters import Filter

from .forms import DateFilterForm


class BaseMonthOfYearFilter(Filter):
    balances_field = ''

    def filter_queryset(self, request, queryset, view):
        form = DateFilterForm(request.GET)
        if form.is_valid():
            month = form.cleaned_data.get('month')
            year = form.cleaned_data.get('year')
            categories_statistics = queryset
            qs_filter = {}
            if month:
                qs_filter[self.balances_field + '__created_at__month'] = month
            if year:
                qs_filter[self.balances_field + '__created_at__year'] = year
            categories_statistics = categories_statistics.filter(**qs_filter)
            return categories_statistics
        return queryset.none()


class SpendingMonthOfYearFilter(BaseMonthOfYearFilter):
    balances_field = 'spendings'


class ProceedMonthOfYearFilter(BaseMonthOfYearFilter):
    balances_field = 'proceeds'

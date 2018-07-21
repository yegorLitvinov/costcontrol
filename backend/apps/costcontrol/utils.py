from django.core.cache import cache
from django.utils.functional import cached_property

from .models import BalanceRecord


class FilledMonthesCache:
    def __init__(self, user):
        self._user = user

    def _generate_filled_months(self):
        filled_months = {}
        for year, month in BalanceRecord.objects.unique_year_month_for(self._user):
            if year not in filled_months:
                filled_months[year] = {}
            filled_months[year][month] = True
        return filled_months

    @cached_property
    def cache_key(self):
        return f"api:{self.__class__.__name__}:user_{self._user.id}"

    def get_filled_months(self):
        filled_months = cache.get(self.cache_key)
        if filled_months is None:
            filled_months = self._generate_filled_months()
            cache.set(self.cache_key, filled_months)
        return filled_months

    def clear(self):
        cache.delete(self.cache_key)

    def add_month(self, date):
        filled_months = self.get_filled_months()
        if date.year not in filled_months:
            filled_months[date.year] = {}
        if date.month not in filled_months[date.year]:
            filled_months[date.year][date.month] = True
            cache.set(self.cache_key, filled_months)

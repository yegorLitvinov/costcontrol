from django.core.cache import cache
from django.utils.functional import cached_property

from .models import BalanceRecord


class FilledMonthesCache:
    def __init__(self, user):
        self._user = user

    def _generate_filled_monthes(self):
        filled_monthes = {}
        for year, month in BalanceRecord.objects.unique_year_month_for(self._user):
            if year not in filled_monthes:
                filled_monthes[year] = {}
            filled_monthes[year][month] = True
        return filled_monthes

    @cached_property
    def cache_key(self):
        return f'api:{self.__class__.__name__}:user_{self._user.id}'

    def get_filled_monthes(self):
        filled_monthes = cache.get(self.cache_key)
        if filled_monthes is None:
            filled_monthes = self._generate_filled_monthes()
            cache.set(self.cache_key, filled_monthes)
        return filled_monthes

    def clear(self):
        cache.delete(self.cache_key)

    def add_month(self, date):
        filled_monthes = self.get_filled_monthes()
        if date.year not in filled_monthes:
            filled_monthes[date.year] = {}
        if date.month not in filled_monthes[date.year]:
            filled_monthes[date.year][date.month] = True
            cache.set(self.cache_key, filled_monthes)

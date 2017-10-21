from django.core.cache import cache

from .models import Proceed, Spending


class FilledMonthesCache():
    def __init__(self):
        # self._user = user
        pass

    def _generate_filled_monthes(self):
        filled_monthes = {}
        for year, month in list(Spending.objects.unique_year_month()) + \
                list(Proceed.objects.unique_year_month()):
            if year not in filled_monthes:
                filled_monthes[year] = {}
            filled_monthes[year][month] = True
        return filled_monthes

    def get_cache_key(self):
        return f'api:{self.__class__.__name__}'

    def get_filled_monthes(self):
        filled_monthes = cache.get(self.get_cache_key())
        if filled_monthes is None:
            filled_monthes = self._generate_filled_monthes()
            cache.set(self.get_cache_key(), filled_monthes)
        return filled_monthes

    def clear(self):
        cache.delete(self.get_cache_key())

    def add_month(self, date):
        filled_monthes = self.get_filled_monthes()
        if date.year not in filled_monthes:
            filled_monthes[date.year] = {}
        if date.month not in filled_monthes[date.year]:
            filled_monthes[date.year][date.month] = True
            cache.set(self.get_cache_key(), filled_monthes)

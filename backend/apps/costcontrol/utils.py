from datetime import datetime

from django.core.cache import cache
from django.utils.functional import cached_property

from .models import BalanceRecord


class FilledMonthesCache:
    def __init__(self, user):
        self._user = user

    def _generate_filled_months(self):
        filled_months = {}
        for year, month in BalanceRecord.objects.unique_year_month_for(self._user):
            filled_months.setdefault(year, {}).setdefault(month, True)
        return filled_months

    @cached_property
    def cache_key(self):
        return f"api:{self.__class__.__name__}:user_{self._user.id}"

    def get_filled_months(self) -> dict:
        filled_months = cache.get(self.cache_key)
        if filled_months is None:
            filled_months = self._generate_filled_months()
            cache.set(self.cache_key, filled_months)
        return filled_months

    def clear(self):
        cache.delete(self.cache_key)

    def add_month(self, date: datetime):
        filled_months = self.get_filled_months()
        filled_months.setdefault(date.year, {}).setdefault(date.month, True)
        cache.set(self.cache_key, filled_months)


class YearMonthCounter:
    def __init__(self, start_year, start_month, reverse=False):
        self.year = start_year
        self.month = start_month
        self.reverse = reverse

    def __next__(self):
        record = {"year": self.year, "month": self.month, "total": 0}
        if self.reverse:
            if self.month == 1:
                self.month = 12
                self.year -= 1
            else:
                self.month -= 1
        else:
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        return record

    def __lt__(self, date):
        if self.year < date.year:
            return True
        if self.month < date.month:
            return True
        return False

    def __eq__(self, date):
        if self.year == date.year and self.month == date.month:
            return True
        return False

    def __gt__(self, date):
        if self.year > date.year:
            return True
        if self.month > date.month:
            return True
        return False

    def __repr__(self):
        return f"(year={self.year}, month={self.month}, reverse={self.reverse})"


def fill_empty_period(records: list, start_date: datetime, end_date: datetime):
    """
    Sometimes there are no added records during month.
    Fill such  monthes with empty values.
    """

    def empty_range():
        counter = YearMonthCounter(start_date.year, start_date.month)
        while counter < end_date or counter == end_date:
            yield next(counter)

    # Create map of {year: {month: total}}, e.g. {2018: {2: 44}}
    year_month_map = {}
    for record in records:
        year_month_map.setdefault(record["year"], {})
        year_month_map[record["year"]][record["month"]] = record["total"]

    results = list(empty_range())
    for result in results:
        try:
            total = year_month_map[result["year"]][result["month"]]
        except KeyError:
            pass
        else:
            result["total"] = total

    # Combine year-month
    results = [
        {
            "year_month": "{}-{:02d}".format(result["year"], result["month"]),
            "total": result["total"],
        }
        for result in results
    ]
    return results

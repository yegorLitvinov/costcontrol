from datetime import datetime


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

    def __eq__(self, date):
        if self.year == date.year and self.month == date.month:
            return True
        return False

    def __lt__(self, date):
        if self.year < date.year:
            return True
        elif self.year > date.year:
            return False
        elif self.month < date.month:
            return True
        return False

    def __le__(self, date):
        return self == date or self < date

    def __repr__(self):
        return f"(year={self.year}, month={self.month}, reverse={self.reverse})"


def fill_empty_period(records: list, start_date: datetime, end_date: datetime) -> list:
    """
    Sometimes there are no added records during month.
    Fill such monthes with empty values.
    """

    def empty_range():
        counter = YearMonthCounter(start_date.year, start_date.month)
        while counter <= end_date:
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


def generate_filled_monthes(start_date: datetime, end_date: datetime) -> dict:
    filled_months = {}
    counter = YearMonthCounter(start_date.year, start_date.month)
    while counter <= end_date:
        filled_months.setdefault(counter.year, {}).setdefault(counter.month, True)
        next(counter)
    return filled_months

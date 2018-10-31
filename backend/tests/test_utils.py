from datetime import datetime
from unittest.mock import MagicMock

import pytz

from apps.costcontrol.factories import ProceedRecordFactory
from apps.costcontrol.utils import FilledMonthesCache, YearMonthCounter, fill_empty_period


def test_year_month_counter():
    counter = YearMonthCounter(2018, 11)
    assert next(counter) == {"year": 2018, "month": 11, "total": 0}
    assert next(counter) == {"year": 2018, "month": 12, "total": 0}
    assert next(counter) == {"year": 2019, "month": 1, "total": 0}
    assert next(counter) == {"year": 2019, "month": 2, "total": 0}

    assert not counter < datetime(2019, 3, 1)
    assert not counter > datetime(2019, 3, 1)
    assert counter < datetime(2019, 5, 1)
    assert counter > datetime(2018, 5, 1)

    counter = YearMonthCounter(2019, 2, reverse=True)
    assert next(counter) == {"year": 2019, "month": 2, "total": 0}
    assert next(counter) == {"year": 2019, "month": 1, "total": 0}
    assert next(counter) == {"year": 2018, "month": 12, "total": 0}
    assert next(counter) == {"year": 2018, "month": 11, "total": 0}


def test_fill_empty_period():
    start_date = datetime(2018, 3, 3)
    end_date = datetime(2018, 9, 3)
    records = fill_empty_period(
        [{"year": 2018, "month": 5, "total": 1}, {"year": 2018, "month": 7, "total": 2}],
        start_date,
        end_date,
    )
    assert records == [
        {"year_month": "2018-03", "total": 0},
        {"year_month": "2018-04", "total": 0},
        {"year_month": "2018-05", "total": 1},
        {"year_month": "2018-06", "total": 0},
        {"year_month": "2018-07", "total": 2},
        {"year_month": "2018-08", "total": 0},
        {"year_month": "2018-09", "total": 0},
    ]


def test_fill_empty_period_one_day():
    start_date = datetime(2018, 3, 3)
    end_date = start_date
    records = fill_empty_period(
        [{"year": 2018, "month": 3, "total": 1}], start_date, end_date
    )
    assert records == [{"year_month": "2018-03", "total": 1}]


def test_fill_empty_period_start_date_more_than_end_date():
    start_date = datetime(2018, 3, 3)
    end_date = datetime(2018, 2, 3)
    records = fill_empty_period(
        [{"year": 2018, "month": 3, "total": 1}], start_date, end_date
    )
    assert records == []


def test_filled_monthes_cache(db, user, monkeypatch):
    cache = FilledMonthesCache(user=user)
    tz = pytz.timezone("Europe/Moscow")
    now_mock = MagicMock(return_value=datetime(2018, 4, 4, tzinfo=tz))
    monkeypatch.setattr("django.utils.timezone.now", now_mock)
    ProceedRecordFactory(category__user=user)

    assert cache.get_filled_months() == {2018: {4: True}}
    cache.add_month(datetime(2018, 3, 3))
    assert cache.get_filled_months() == {2018: {3: True, 4: True}}
    cache.add_month(datetime(2019, 1, 1))
    assert cache.get_filled_months() == {2018: {3: True, 4: True}, 2019: {1: True}}
    cache.clear()
    assert cache.get_filled_months() == {2018: {4: True}}
    cache.clear()

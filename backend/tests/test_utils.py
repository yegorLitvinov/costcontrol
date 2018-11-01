from datetime import datetime

from apps.costcontrol.utils import (
    YearMonthCounter,
    fill_empty_period,
    generate_filled_monthes,
)


def test_year_month_counter():
    counter = YearMonthCounter(2018, 11)
    assert counter <= datetime(2019, 1, 1)

    assert next(counter) == {"year": 2018, "month": 11, "total": 0}
    assert next(counter) == {"year": 2018, "month": 12, "total": 0}
    assert next(counter) == {"year": 2019, "month": 1, "total": 0}
    assert next(counter) == {"year": 2019, "month": 2, "total": 0}

    assert counter == datetime(2019, 3, 22)
    assert not (counter < datetime(2019, 3, 1))
    assert counter < datetime(2019, 5, 1)

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


def test_generate_filled_monthes():
    assert generate_filled_monthes(datetime(2018, 11, 1), datetime(2018, 11, 30)) == {
        2018: {11: True}
    }
    assert generate_filled_monthes(datetime(2018, 11, 1), datetime(2018, 12, 30)) == {
        2018: {11: True, 12: True}
    }

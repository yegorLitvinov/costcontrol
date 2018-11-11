from datetime import timedelta
from unittest import mock

import pytest
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.factories import UserFactory
from apps.costcontrol.factories import (
    BalanceRecordFactory,
    ProceedCategoryFactory,
    ProceedRecordFactory,
    SpendingCategoryFactory,
    SpendingRecordFactory,
)


@pytest.mark.parametrize("url", ["history", "filled-months"])
def test_common_get_anonym(db, url):
    client = APIClient()
    response = client.get(f"/api/costcontrol/{url}/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize("url", ["history", "filled-months"])
def test_filled_months_post(db, user, url):
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(f"/api/costcontrol/{url}/")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_proceed_get_anonym(db):
    proceed = ProceedRecordFactory()
    client = APIClient()
    response = client.get(f"/api/costcontrol/balance-record/{proceed.pk}/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_proceed_get_another_user(db):
    user1, user2 = UserFactory.create_batch(2)
    category = ProceedCategoryFactory(user=user1)
    proceed = ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get(f"/api/costcontrol/balance-record/{proceed.pk}/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_history_get_another_user(db):
    user1, user2 = UserFactory.create_batch(2)
    category = ProceedCategoryFactory(user=user1)
    ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get("/api/costcontrol/history/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"count": 0, "next": None, "previous": None, "results": []}


def test_history_filter(db):
    user = UserFactory()
    category1, category2 = ProceedCategoryFactory.create_batch(2, user=user)

    proceed = ProceedRecordFactory(category=category1)
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/costcontrol/history/", dict(category=543534534))
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client.get("/api/costcontrol/history/", dict(category=category2.id))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 0

    response = client.get("/api/costcontrol/history/", dict(category=category1.id))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    assert response.data["results"][0]["id"] == proceed.id


def test_history_search(db):
    user = UserFactory()
    proceed = ProceedRecordFactory(category__user=user, comment="Juice")
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/costcontrol/history/", dict(search=""))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    assert response.data["results"][0]["id"] == proceed.id

    response = client.get("/api/costcontrol/history/", dict(search="Bread"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 0

    response = client.get("/api/costcontrol/history/", dict(search="Ice"))
    assert response.status_code == status.HTTP_200_OK
    assert response.data["count"] == 1
    assert response.data["results"][0]["id"] == proceed.id


def test_year_statistics(db, user):
    now = timezone.datetime(2018, 1, 3, tzinfo=timezone.get_current_timezone())
    two_month_later = now + timedelta(days=60)
    with mock.patch("django.utils.timezone.now") as now_mock:
        now_mock.return_value = now
        SpendingRecordFactory(category__user=user, amount=50)
        ProceedRecordFactory.create_batch(2, category__user=user, amount=100)
        now_mock.return_value = two_month_later
        ProceedRecordFactory(category__user=user, amount=25)

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/costcontrol/year-statistics/")
    assert response.status_code == 400
    assert response.data == {"year": ["This field is required."]}

    response = client.get("/api/costcontrol/year-statistics/?year=18")
    assert response.status_code == 400
    assert response.data == {
        "year": ["Ensure this value is greater than or equal to 1990."]
    }

    response = client.get("/api/costcontrol/year-statistics/?year=")
    assert response.status_code == 400
    assert response.data == {"year": ["A valid integer is required."]}

    response = client.get("/api/costcontrol/year-statistics/?year=string")
    assert response.status_code == 400
    assert response.data == {"year": ["A valid integer is required."]}

    response = client.get(f"/api/costcontrol/year-statistics/?year={now.year}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {"month": now.month, "category__kind": "proceed", "total": 200},
        {"month": now.month, "category__kind": "spending", "total": 50},
        {"month": two_month_later.month, "category__kind": "proceed", "total": 25},
    ]


def test_category_statistics(db, user):
    now = timezone.now()
    category = SpendingCategoryFactory(user=user)
    BalanceRecordFactory(category=category, amount=123)

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f"/api/costcontrol/categories/{category.id}/year_statistics/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{"year_month": f"{now.year}-{now.month}", "total": 123}]


def test_total(db, user):
    ProceedRecordFactory(category__user=user, amount=302)
    SpendingRecordFactory(category__user=user, amount=102)
    SpendingRecordFactory(amount=100)
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/costcontrol/total/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"accumulated": 200}

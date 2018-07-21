from unittest import mock

import pytest
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.factories import UserFactory
from apps.costcontrol.factories import (ProceedCategoryFactory, ProceedRecordFactory,
                                        SpendingRecordFactory)


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
    response = client.get(f"/api/costcontrol/history/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "count": 0,
        "next": None,
        "previous": None,
        "results": [],
    }


def test_filled_months_get_another_user(db):
    user1, user2 = UserFactory.create_batch(2)
    category = ProceedCategoryFactory(user=user1)
    ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get(f"/api/costcontrol/filled-months/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {}


def test_filled_months_get_success(db, user):
    category = ProceedCategoryFactory(user=user)
    ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f"/api/costcontrol/filled-months/")
    assert response.status_code == status.HTTP_200_OK
    now = timezone.now()
    assert response.json() == {str(now.year): {str(now.month): True}}


def test_year_statistics(db, user):
    now = timezone.datetime(2018, 1, 3, tzinfo=timezone.get_current_timezone())
    two_month_later = now + timezone.timedelta(days=60)
    with mock.patch("django.utils.timezone.now") as now_mock:
        now_mock.return_value = now
        SpendingRecordFactory(category__user=user, amount=50)
        ProceedRecordFactory.create_batch(2, category__user=user, amount=100)
        now_mock.return_value = two_month_later
        ProceedRecordFactory(category__user=user, amount=25)

    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f"/api/costcontrol/year-statistics/?year={now.year}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {"month": now.month, "category__kind": "proceed", "total": 200},
        {"month": now.month, "category__kind": "spending", "total": 50},
        {"month": two_month_later.month, "category__kind": "proceed", "total": 25},
    ]

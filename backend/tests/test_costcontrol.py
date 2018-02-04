import pytest
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.factories import UserFactory
from apps.costcontrol.factories import ProceedCategoryFactory, ProceedRecordFactory


@pytest.mark.parametrize('url', ['history', 'filled-months'])
def test_common_get_anonym(db, url):
    client = APIClient()
    response = client.get(f'/api/costcontrol/{url}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.parametrize('url', ['history', 'filled-months'])
def test_filled_months_post(db, user, url):
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(f'/api/costcontrol/{url}/')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_proceed_get_anonym(db):
    proceed = ProceedRecordFactory()
    client = APIClient()
    response = client.get(f'/api/costcontrol/balance-record/{proceed.pk}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_proceed_get_another_user(db):
    user1, user2 = UserFactory.create_batch(2)
    category = ProceedCategoryFactory(user=user1)
    proceed = ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get(f'/api/costcontrol/balance-record/{proceed.pk}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_history_get_another_user(db):
    user1, user2 = UserFactory.create_batch(2)
    category = ProceedCategoryFactory(user=user1)
    ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get(f'/api/costcontrol/history/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == []


def test_filled_months_get_another_user(db):
    user1, user2 = UserFactory.create_batch(2)
    category = ProceedCategoryFactory(user=user1)
    ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get(f'/api/costcontrol/filled-months/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {}


def test_filled_months_get_success(db, user):
    category = ProceedCategoryFactory(user=user)
    ProceedRecordFactory(category=category)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f'/api/costcontrol/filled-months/')
    assert response.status_code == status.HTTP_200_OK
    now = timezone.now()
    assert response.json() == {str(now.year): {str(now.month): True}}

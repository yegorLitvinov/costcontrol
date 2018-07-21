import pytest
from knox.models import AuthToken
from rest_framework.test import APIClient

from apps.accounts.factories import UserFactory


@pytest.fixture
def user(db):
    u = UserFactory(email="alex@black.com")
    u.set_password("password")
    u.save()
    return u


@pytest.fixture
def client(user):
    token_str = AuthToken.objects.create(user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + token_str)
    return client

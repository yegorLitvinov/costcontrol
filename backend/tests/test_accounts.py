from base64 import b64encode

from knox.models import AuthToken
from rest_framework import status
from rest_framework.test import APIClient


def test_login_wrong_methods(db):
    client = APIClient()
    response = client.get('/api/accounts/login/')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    response = client.put('/api/accounts/login/')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    response = client.patch('/api/accounts/login/')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    response = client.delete('/api/accounts/login/')
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_login_no_auth_header(db):
    client = APIClient()
    response = client.post('/api/accounts/login/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_login_success(db, user):
    client = APIClient()
    base64_bytes = b64encode(f'{user.email}:password'.encode())
    response = client.post(
        '/api/accounts/login/',
        HTTP_AUTHORIZATION='Basic ' + base64_bytes.decode()
    )

    assert response.status_code == status.HTTP_200_OK
    # assert response['WWW-Authenticate'] == 'CustomBasic realm=api'
    assert response.data['token']
    assert response.data['user']['id'] == user.id
    assert response.data['user']['first_name'] == user.first_name

    tokens = AuthToken.objects.all()
    assert len(tokens) == 1
    token = tokens[0]
    assert token.token_key in response.data['token']
    assert token.user == user


def test_logout(db, client):
    assert AuthToken.objects.all().count() == 1
    response = client.post('/api/accounts/logout/')
    assert response.status_code == status.HTTP_204_NO_CONTENT

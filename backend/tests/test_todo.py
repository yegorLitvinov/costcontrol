import pytest
from rest_framework import status
from rest_framework.test import APIClient

from apps.accounts.factories import UserFactory
from apps.todo.factories import TodoFactory


@pytest.fixture
def user(db):
    return UserFactory(email='alex@black.com', password='password')


@pytest.fixture
def todo(user):
    return TodoFactory(user=user)


def test_unauthorized(db, todo):
    client = APIClient()
    response = client.get(f'/api/todo/todo/{todo.id}/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_success_get(db, user, todo):
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.get(f'/api/todo/todo/{todo.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == todo.id
    assert response.data['text'] == todo.text
    assert not response.data['completed']


def test_not_owner(db, user, todo):
    client = APIClient()
    user2 = UserFactory()

    client.force_authenticate(user=user2)
    response = client.get(f'/api/todo/todo/{todo.id}/')

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_order(db, user):
    client = APIClient()
    todo2 = TodoFactory(user=user)
    TodoFactory.create_batch(3, user=user)
    todo1 = TodoFactory(user=user, completed=True)
    todo2.text = 'New text'
    todo2.save()

    client.force_authenticate(user=user)
    response = client.get(f'/api/todo/todo/')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5
    assert response.data[4]['id'] == todo1.id
    assert response.data[0]['id'] == todo2.id


def test_partial_update(db, user, todo):
    client = APIClient()

    client.force_authenticate(user=user)
    response = client.patch(f'/api/todo/todo/{todo.id}/', {
        'text': 'some text'
    })

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == todo.id
    assert response.data['text'] == 'some text'
    assert not response.data['completed']

    client.force_authenticate(user=user)
    response = client.patch(f'/api/todo/todo/{todo.id}/', {
        'completed': True
    })

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == todo.id
    assert response.data['text'] == 'some text'
    assert response.data['completed']

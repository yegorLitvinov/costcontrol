from base64 import b64encode
from datetime import date

import django
django.setup()  # noqa
from locust import HttpLocust, TaskSet, task

from apps.accounts.models import User


class UserTasks(TaskSet):
    def on_start(self):
        user, _ = User.objects.get_or_create(
            email='test@example.com',
            username='test',
            first_name='First Name',
            last_name='Last Name'
        )
        user.set_password('password')
        user.save()
        base64_bytes = b64encode(f'{user.email}:password'.encode())
        response = self.client.post('/api/accounts/login/', headers={
            'Authorization': 'Basic ' + base64_bytes.decode()
        })
        self._token = response.json()['token']
        self._date = date(2017, 7, 15)

    @task
    def category_statistics(self):
        self.client.get(
            '/api/costcontrol/categories/statistics/',
            params={
                'year': self._date.year,
                'month': self._date.month,
                'kind': 'spending'
            },
            headers={
                'Authorization': 'Token ' + self._token
            }
        )


class WebsiteUser(HttpLocust):
    task_set = UserTasks
    host = 'http://localhost:8000'
    min_wait = 100
    max_wait = 1000

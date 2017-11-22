import factory

from apps.accounts.factories import UserFactory

from .models import Todo


class TodoFactory(factory.DjangoModelFactory):
    class Meta:
        model = Todo

    text = factory.Faker('word')
    user = factory.SubFactory(UserFactory)

import factory

from .models import User


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('last_name')

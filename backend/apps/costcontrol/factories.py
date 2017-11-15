import factory

from apps.accounts.factories import UserFactory

from .models import Category


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    color = 'red'
    icon = factory.django.ImageField()
    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)


class ProceedCategoryFactory(CategoryFactory):
    kind = Category.KIND_PROCEED


class SpendingCategoryFactory(CategoryFactory):
    kind = Category.KIND_SPENDING

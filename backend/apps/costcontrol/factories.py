import factory

from apps.accounts.factories import UserFactory

from .models import BalanceRecord, Category


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    color = "red"
    icon = factory.django.ImageField()
    name = factory.Faker("word")
    user = factory.SubFactory(UserFactory)


class ProceedCategoryFactory(CategoryFactory):
    kind = Category.KIND_PROCEED


class SpendingCategoryFactory(CategoryFactory):
    kind = Category.KIND_SPENDING


class BalanceRecordFactory(factory.DjangoModelFactory):
    class Meta:
        model = BalanceRecord

    amount = factory.Faker("pyint")
    comment = factory.Faker("word")


class ProceedRecordFactory(BalanceRecordFactory):
    category = factory.SubFactory(ProceedCategoryFactory)


class SpendingRecordFactory(BalanceRecordFactory):
    category = factory.SubFactory(SpendingCategoryFactory)

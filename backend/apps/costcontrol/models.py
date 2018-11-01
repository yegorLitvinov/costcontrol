from django.conf import settings
from django.db import models

from apps.core.models import AppModel, TimeStampedMixin


class Category(AppModel):
    owner = "user"

    KIND_PROCEED = "proceed"
    KIND_SPENDING = "spending"
    KIND_CHOICES = ((KIND_PROCEED, "Proceed"), (KIND_SPENDING, "Spending"))

    color = models.CharField(max_length=64)
    icon = models.ImageField(upload_to="icons")
    kind = models.CharField(max_length=10, choices=KIND_CHOICES)
    name = models.CharField(max_length=256)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="categories", on_delete=models.PROTECT
    )

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"{self.name} ({self.kind})"


class BalanceRecord(TimeStampedMixin, AppModel):
    owner = "category__user"

    amount = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category, related_name="balance_records", on_delete=models.PROTECT
    )
    comment = models.CharField(max_length=256, blank=True)

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"{self.amount} \u20bd {self.comment}"

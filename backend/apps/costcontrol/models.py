from django.conf import settings
from django.db import models
from django.db.models.functions import ExtractMonth, ExtractYear

from apps.core.models import TimeStampedModel


class Category(models.Model):
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


class BalanceRecordQuerySet(models.QuerySet):
    def unique_year_month_for(self, user):
        return (
            self.filter(category__user=user)
            .annotate(year=ExtractYear("created_at"), month=ExtractMonth("created_at"))
            .values_list("year", "month")
            .distinct()
        )


class BalanceRecord(TimeStampedModel):
    amount = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category, related_name="balance_records", on_delete=models.PROTECT
    )
    comment = models.CharField(max_length=256, blank=True)

    objects = BalanceRecordQuerySet.as_manager()

    class Meta:
        ordering = ["pk"]

    def __str__(self):
        return f"{self.amount} \u20bd {self.comment}"

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import BalanceRecord
from .utils import FilledMonthesCache


@receiver(post_save, sender=BalanceRecord)
def update_filled_months(sender, instance, *args, **kwargs):
    FilledMonthesCache(instance.category.user).add_month(timezone.now())

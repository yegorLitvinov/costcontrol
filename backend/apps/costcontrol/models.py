from django.conf import settings
from django.db import models
from django.db.models.functions import ExtractMonth, ExtractYear


class BaseCategory(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='icons')

    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):
        return self.name


class SpendingCategory(BaseCategory):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='spending_categories')


class ProceedCategory(BaseCategory):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='proceed_categories')


class BalanceRecord(models.Model):
    amount = models.PositiveIntegerField()
    comment = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):
        return f'{self.amount} RUB {self.comment}'

    @staticmethod
    def get_last_records(cnt):
        """Return formated list of dicts."""
        spendings = (Spending.objects.all()
                     .select_related('category')
                     .order_by('-created_at')
                     .values('amount', 'comment', 'created_at', 'category__name')[:cnt])
        for spending in spendings:
            spending['sign'] = '-'

        proceeds = (Proceed.objects.all()
                    .select_related('category')
                    .order_by('-created_at')
                    .values('amount', 'comment', 'created_at', 'category__name')[:cnt])
        for proceed in proceeds:
            proceed['sign'] = '+'

        balance_records = list(spendings) + list(proceeds)
        balance_records.sort(
            key=lambda record: record['created_at'], reverse=True)
        balance_records = balance_records[:cnt]

        for record in balance_records:
            record['created_at'] = record['created_at'].strftime('%d %b')
        return balance_records


class BalanceRecordQuerySet(models.QuerySet):
    def unique_year_month(self):
        return self.annotate(year=ExtractYear('created_at'), month=ExtractMonth('created_at')) \
            .values_list('year', 'month') \
            .distinct()


class Spending(BalanceRecord):
    category = models.ForeignKey(SpendingCategory, related_name='spendings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='spendings')

    objects = BalanceRecordQuerySet.as_manager()

    def __str__(self):
        return '- ' + super().__str__()


class Proceed(BalanceRecord):
    category = models.ForeignKey(ProceedCategory, related_name='proceeds')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='proceeds')

    objects = BalanceRecordQuerySet.as_manager()

    def __str__(self):
        return '+ ' + super().__str__()

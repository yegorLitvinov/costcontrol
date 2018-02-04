from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel


class Todo(TimeStampedModel):
    completed = models.BooleanField(default=False)
    text = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='todos')

    class Meta:
        ordering = ('completed', '-updated_at')

    def __str__(self):
        completed = "(completed)" if self.completed else ''
        return f'{completed} {self.text}'

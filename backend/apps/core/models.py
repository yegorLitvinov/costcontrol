from django.db import models


class AppModelMeta(type(models.Model)):
    def __new__(cls, *args):
        new_class = super().__new__(cls, *args)
        if not new_class._meta.abstract:
            assert hasattr(new_class, "owner"), "Model must have 'owner' attribute."
        return new_class


class AppModel(models.Model, metaclass=AppModelMeta):
    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

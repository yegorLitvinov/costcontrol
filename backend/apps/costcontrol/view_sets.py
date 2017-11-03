from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Proceed, ProceedCategory, Spending, SpendingCategory
from .utils import FilledMonthesCache
from .serializers import (ProceedCategorySerializer, ProceedSerializer, SpendingCategorySerializer,
                          SpendingSerializer)
from .view_mixins import OwnerMixin


class UpdateCacheMixin:
    """
    Update cache when model has changed.
    """

    def perform_create(self, serializer):
        super().perform_create(serializer)
        FilledMonthesCache(self.request.user).add_month(timezone.now())


class SpendingCategoryViewSet(OwnerMixin, viewsets.ModelViewSet):
    serializer_class = SpendingCategorySerializer
    queryset = SpendingCategory.objects.all()
    permission_classes = [IsAuthenticated]


class ProceedCategoryViewSet(OwnerMixin, viewsets.ModelViewSet):
    serializer_class = ProceedCategorySerializer
    queryset = ProceedCategory.objects.all()
    permission_classes = [IsAuthenticated]


class SpendingViewSet(UpdateCacheMixin, OwnerMixin, viewsets.ModelViewSet):
    serializer_class = SpendingSerializer
    queryset = Spending.objects.all()
    permission_classes = [IsAuthenticated]


class ProceedViewSet(UpdateCacheMixin, OwnerMixin, viewsets.ModelViewSet):
    serializer_class = ProceedSerializer
    queryset = Proceed.objects.all()
    permission_classes = [IsAuthenticated]
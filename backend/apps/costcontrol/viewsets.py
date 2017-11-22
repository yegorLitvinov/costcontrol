from django.utils import timezone
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import BalanceRecord, Category
from .serializers import BalanceRecordSerializer, CategorySerializer
from .utils import FilledMonthesCache
from .view_mixins import OwnerMixin


class UpdateCacheMixin:
    """
    Update cache when model has changed.
    """

    def perform_create(self, serializer):
        super().perform_create(serializer)
        FilledMonthesCache(self.request.user).add_month(timezone.now())


class CategoryViewSet(OwnerMixin, viewsets.ModelViewSet):
    filter_fields = ['kind']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class BalanceRecordViewSet(UpdateCacheMixin, viewsets.ModelViewSet):
    serializer_class = BalanceRecordSerializer
    queryset = BalanceRecord.objects.all()
    permission_classes = [IsAuthenticated]

from django.db.models import Sum
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from apps.core.view_mixins import OwnerMixin

from .filters import MonthOfYearFilter
from .models import BalanceRecord, Category
from .permissions import IsCategoryOwner, IsRecordOwner
from .serializers import (BalanceRecordSerializer, CategorySerializer,
                          CategoryStatisticSerializer)
from .utils import FilledMonthesCache
from .view_mixins import BalanceRecordOwnerMixin


class CategoryStatisticListView(OwnerMixin, generics.ListAPIView):
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [MonthOfYearFilter]
    filter_fields = ['kind']
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategoryStatisticSerializer

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.annotate(
            total=Sum('balance_records__amount')
        )


class HistoryView(BalanceRecordOwnerMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BalanceRecord.objects.all()
    serializer_class = BalanceRecordSerializer

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        qs = qs.order_by('-created_at')[:20]
        return qs


class FilledMonthesView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        filled_months = FilledMonthesCache(request.user).get_filled_months()
        return JsonResponse(filled_months)


class CategoryViewSet(OwnerMixin, viewsets.ModelViewSet):
    filter_fields = ['kind']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsCategoryOwner]


class BalanceRecordViewSet(BalanceRecordOwnerMixin, viewsets.ModelViewSet):
    serializer_class = BalanceRecordSerializer
    queryset = BalanceRecord.objects.all()
    permission_classes = [IsRecordOwner]

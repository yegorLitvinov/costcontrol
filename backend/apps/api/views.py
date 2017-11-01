from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.views import APIView
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.settings import api_settings

from apps.costcontrol.models import BalanceRecord, ProceedCategory, SpendingCategory
from apps.costcontrol.utils import FilledMonthesCache

from .filters import ProceedMonthOfYearFilter, SpendingMonthOfYearFilter
from .serializers import (ProceedCategoryStatisticSerializer, SpeindingCategoryStatisticSerializer,
                          UserSerializer)
from .view_mixins import OwnerMixin


class CustomBasicAuth(BasicAuthentication):
    def authenticate_header(self, request):
        return f'CustomBasic realm={self.www_authenticate_realm}'


class LoginView(KnoxLoginView):
    authentication_classes = (CustomBasicAuth,)
    permission_classes = (AllowAny,)
    allowed_methods = ('post',)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        return super().post(request, format)


class SpendingCategoryStatisticListView(OwnerMixin, generics.ListAPIView):
    serializer_class = SpeindingCategoryStatisticSerializer
    queryset = SpendingCategory.objects.all()
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + \
        [SpendingMonthOfYearFilter]
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        spending_statistics = super().filter_queryset(queryset)
        return spending_statistics.annotate(
            total=Sum('spendings__amount')
        )


class ProceedCategoryStatisticListView(OwnerMixin, generics.ListAPIView):
    serializer_class = ProceedCategoryStatisticSerializer
    queryset = ProceedCategory.objects.all()
    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + \
        [ProceedMonthOfYearFilter]
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        proceed_statistics = super().filter_queryset(queryset)
        return proceed_statistics.annotate(
            total=Sum('proceeds__amount')
        )


class HistoryView(OwnerMixin, APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, cnt, *args, **kwargs):
        cnt = int(cnt) if cnt else 10
        last_records = BalanceRecord.get_last_records(cnt)
        return JsonResponse(last_records, safe=False)


class FilledMonthesView(APIView):
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        filled_monthes = FilledMonthesCache().get_filled_monthes()
        return JsonResponse(filled_monthes, safe=False)

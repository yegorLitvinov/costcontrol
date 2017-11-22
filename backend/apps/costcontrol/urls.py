from django.conf.urls import url
from rest_framework import routers

from .views import CategoryStatisticListView, FilledMonthesView, HistoryView
from .viewsets import BalanceRecordViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'balance-record', BalanceRecordViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(r'^category/statistic/', CategoryStatisticListView.as_view(), name='statistics'),
    url(r'^history/', HistoryView.as_view(), name='history'),
    url(r'^filled-monthes/', FilledMonthesView.as_view(), name='filled_monthes'),
] + router.urls

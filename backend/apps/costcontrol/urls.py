from django.conf.urls import url
from rest_framework import routers

from .views import (BalanceRecordViewSet, CategoryStatisticsListView, CategoryViewSet,
                    FilledMonthesView, HistoryView, YearStatisticsListView)

router = routers.DefaultRouter()
router.register(r'balance-record', BalanceRecordViewSet)
router.register(r'category', CategoryViewSet)

urlpatterns = [
    url(
        r'^category/statistics/',
        CategoryStatisticsListView.as_view(),
        name='statistics'
    ),
    url(
        r'^year-statistics/',
        YearStatisticsListView.as_view(),
        name='year_statistics'
    ),
    url(r'^history/', HistoryView.as_view(), name='history'),
    url(r'^filled-months/', FilledMonthesView.as_view(), name='filled_months'),
] + router.urls

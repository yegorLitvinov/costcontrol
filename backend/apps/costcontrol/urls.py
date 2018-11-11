from django.conf.urls import url
from rest_framework import routers

from .views import (
    BalanceRecordViewSet,
    CategoryStatisticsListView,
    CategoryViewSet,
    FilledMonthesView,
    HistoryView,
    TotalView,
    YearStatisticsListView,
)

app_name = "costcontrol"

router = routers.DefaultRouter()
router.register(r"balance-record", BalanceRecordViewSet)
router.register(r"categories", CategoryViewSet)

urlpatterns = [
    url(
        r"^categories/statistics/",
        CategoryStatisticsListView.as_view(),
        name="statistics",
    ),
    url(r"^year-statistics/", YearStatisticsListView.as_view(), name="year_statistics"),
    url(r"^history/", HistoryView.as_view(), name="history"),
    url(r"^filled-months/", FilledMonthesView.as_view(), name="filled_months"),
    url(r"^total/", TotalView.as_view(), name="total"),
] + router.urls

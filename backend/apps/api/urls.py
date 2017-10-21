from django.conf.urls import url
from knox.views import LogoutView
from rest_framework import routers

from .view_sets import ProceedCategoryViewSet, ProceedViewSet, SpendingCategoryViewSet, SpendingViewSet
from .views import (FilledMonthesView, HistoryView, LoginView, ProceedCategoryStatisticListView,
                    SpendingCategoryStatisticListView)

router = routers.DefaultRouter()
router.register(r'spending', SpendingViewSet, 'spending')
router.register(r'proceed', ProceedViewSet, 'proceed')
router.register(r'category/spending', SpendingCategoryViewSet, 'category_spending')
router.register(r'category/proceed', ProceedCategoryViewSet, 'category_proceed')

urlpatterns = router.urls + [
    url(r'^accounts/login/', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/', LogoutView.as_view(), name='logout'),
    url(r'^statistic/spending', SpendingCategoryStatisticListView.as_view(), name='statistics_spending'),
    url(r'^statistic/proceed', ProceedCategoryStatisticListView.as_view(), name='statistics_proceed'),
    url(r'^history/(?P<cnt>\d*)', HistoryView.as_view(), name='history'),
    url(r'^filled-monthes/', FilledMonthesView.as_view(), name='filled_monthes'),
]

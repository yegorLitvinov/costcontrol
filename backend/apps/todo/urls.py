from rest_framework.routers import DefaultRouter

from .viewsets import TodoViewSet

router = DefaultRouter()
router.register('todo', TodoViewSet)

urlpatterns = router.urls

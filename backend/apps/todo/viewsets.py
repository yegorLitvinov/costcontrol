from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.core.view_mixins import OwnerMixin

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(OwnerMixin, ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]

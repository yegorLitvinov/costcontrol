from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

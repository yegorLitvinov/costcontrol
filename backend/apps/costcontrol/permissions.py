from rest_framework.permissions import IsAuthenticated


class IsCategoryOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsRecordOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.category.user == request.user

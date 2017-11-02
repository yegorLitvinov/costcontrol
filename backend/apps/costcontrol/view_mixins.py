class OwnerMixin:
    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.filter(user=self.request.user)

class BalanceRecordOwnerMixin:
    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        return qs.filter(category__user=self.request.user)

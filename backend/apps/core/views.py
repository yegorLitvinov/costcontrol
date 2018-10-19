class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(**{qs.model.owner: self.request.user})

from django.apps import AppConfig


class CostcontrolConfig(AppConfig):
    name = "apps.costcontrol"

    def ready(self):
        import apps.costcontrol.signals  # noqa

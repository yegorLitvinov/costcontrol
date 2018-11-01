from .base import *  # noqa

DEBUG = False
ALLOWED_HOSTS = [".tvgun.ga"]
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (  # noqa
    "rest_framework.renderers.JSONRenderer",
)

from .base import *  # noqa

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += ["apps.cypress"]  # noqa

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

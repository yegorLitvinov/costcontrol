from .dev import *  # noqa

DATABASES["default"]["HOST"] = "db"  # noqa
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

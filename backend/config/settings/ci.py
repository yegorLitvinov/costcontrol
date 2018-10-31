from .dev import *  # noqa

DATABASES["default"]["HOST"] = "db"  # noqa
CACHES["default"]["LOCATION"] = "cache:11211"  # noqa
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

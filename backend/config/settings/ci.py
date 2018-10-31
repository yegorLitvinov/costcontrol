from .dev import *  # noqa

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "costcontrol",
        "USER": "costcontrol",
        "PASSWORD": "costcontrol",
        "HOST": "db",
        "PORT": "",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "LOCATION": "cache:11211",
        "TIMEOUT": 60 * 60 * 24 * 30,
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

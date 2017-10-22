from .base import *  # noqa

ALLOWED_HOSTS = [
    'costcontrol.ddns.net',
]

DATABASES['default']['HOST'] = 'postgres'  # noqa
CACHES['default']['LOCATION'] = 'memcached:11211'  # noqa

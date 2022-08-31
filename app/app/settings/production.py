from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "swinemovementdb",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres",
        "PORT": "5432",
        "CONN_MAX_AGE": None,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SOCKET_CONNECT_TIMEOUT": 1,  # in seconds
            "SOCKET_TIMEOUT": 1,  # in seconds
        },
        "KEY_PREFIX": "swinemovement",
    },
}

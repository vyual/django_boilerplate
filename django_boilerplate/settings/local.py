from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
]

CELERY_BROKER_URL = "redis://cache:6379/0"

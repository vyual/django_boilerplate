from .base import *

DEBUG = False

ALLOWED_HOSTS = ["*"]

CELERY_BROKER_URL = "redis://cache:6379/0"

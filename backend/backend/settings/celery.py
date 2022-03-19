import os
import django
from django.conf import settings
from celery import Celery
#from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings.production')
django.setup()
#USED CELERY
app = Celery("tasks", broker="redis://localhost:6379")
#USED SQS
#app = Celery("backend", broker="sqs://AKIAVLITHD37AEZO4HLQ:op6UqLdgPKz6JeCGCH5pkmaQcEAnhDtIX5zUyKJl@",include=['nametask.tasks'])


app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks(settings.INSTALLED_APPS)
app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)

import os 
from celery import Celery

app = Celery("mohcough")
from . import settings
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(['recording'])
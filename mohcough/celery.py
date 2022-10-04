import os 
import celery

from mohcough import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mohcough.settings')
app = celery.Celery("mohcough")

app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks(['recording'])

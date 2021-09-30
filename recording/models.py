from django.db import models
import uuid

# Create your models here.
def upload_to(instance, filename):

    return f"recording/cough/{filename}.wav"
    
class Cough(models.Model):
    cough_id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False,unique=True)
    cough_record = models.FileField(upload_to=upload_to)
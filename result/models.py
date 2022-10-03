from __future__ import unicode_literals
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from accounts.models import Subject
from recording.models import AudioRecord

class DiagnoseResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    audio_record = models.OneToOneField(AudioRecord, on_delete=models.CASCADE, null=True)
    covid_status = models.CharField(max_length=50)
    confidence_rate = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)  
from __future__ import unicode_literals
from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from accounts.models import Subject

class DiagnoseResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    covid_status = models.CharField(max_length=50)
    confidence_rate = models.IntegerField()
    phone_number = models.CharField(max_length=11)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)  

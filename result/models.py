from __future__ import unicode_literals
from django.db import models
import uuid
from django.utils.translation import ugettext_lazy as _
from accounts.models import Subject

COVID_STATUS = [
    ('Positive', 'Positive'),
    ('Negative', 'Negative'),
]

class DiagnoseResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    covid_status = models.CharField(choices=COVID_STATUS, max_length=8)
    confidence_rate = models.DecimalField(decimal_places=2, max_digits=3)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)  

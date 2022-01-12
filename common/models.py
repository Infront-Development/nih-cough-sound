from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import gettext_lazy as _
from accounts.models import Subjects
import uuid






class feedback(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE,null=True)
    rating = models.CharField(max_length=200 ,default="")
    remarks = models.CharField(max_length=200, default="",verbose_name=_('Description'))

    def __str__(self):
        return self.rating
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import Subject
import uuid
from django.utils.safestring import mark_safe


rating_choice = [
    ("1", mark_safe('<span class="fa fa-star checked mr-1 text-left" style="color:orange"></span>'*1)),
    ("2", mark_safe('<span class="fa fa-star checked mr-1 text-left" style="color:orange"></span>'*2)),
    ("3", mark_safe('<span class="fa fa-star checked mr-1 text-left" style="color:orange"></span>'*3)),
    ("4", mark_safe('<span class="fa fa-star checked mr-1 text-left" style="color:orange"></span>'*4)),
    ("5", mark_safe('<span class="fa fa-star checked mr-1 text-left" style="color:orange"></span>'*5)),
]

class Feedback(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    rating = models.PositiveSmallIntegerField(max_length=200 ,default=5,
                validators=[MinValueValidator(1), MaxValueValidator(5)],
                verbose_name=_(mark_safe('<span class="font-weight-bold text-dark">Rating:</span>')))
    remarks = models.TextField(max_length=200, default= None, verbose_name=_(mark_safe('<span class="font-weight-bold text-dark">Description:</span>')))
    
    def __str__(self):
        return self.rating
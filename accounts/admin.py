from subjects.models import questionnairedata
from django.contrib import admin
#from .models import *
from subjects.forms import questionnairedata
from subjects.models import questionnairedata

# Register your models here.
@admin.register(questionnairedata)
class questionnaireadmin(admin.ModelAdmin):
    list_display = ['respondent_choices', 'respondent_sex', 'age', 'med_cond_opt', 'respondent_smoke', 'symptoms_opt', 'date_diagnosed']
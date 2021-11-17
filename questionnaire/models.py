from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _, ugettext_lazy 
from django.utils.translation import ugettext_lazy as _
from accounts.models import Subjects


respondent_choices = [
    ("healthy", _("Healthy individual")),
    ("positive", _("COVID-19 (currently positive)")),
    ("negative", _("COVID-19 (currently negative)")),
    

]

respondent_vaccine =[
    ('vaccinated', _('Vaccinated')),
    ('not vaccinated', _('Not Vaccinated'))
]

respondent_sex = [
    ('male', _('Male')),
    ('female', _('Female'))
]

respondent_smoke = [
    ("never", _("Never smoked")),
    ("exsmoker", _("Ex-smoker")),
    ("current1", _("Current smoker (less than one a day)")),
    ("current2", _("Current smoker (1 to 10 cigarettes per day)")),
    ("current3", _("Current smoker (11 to 20 cigarettes per day)")),
    ("current4", _("Current smoker (21+ cigarettes per day)")),
    ("current5", _("Current smoker (e-cigarettes only)")),
]

# date_diagnosed = [
#     ("none", _("none")),
#     ("last14days", _("Within last 14 days")),
#     ("morethan14days", _("More than 14 days ago, less than 3 months")),
#     ("morethan3m", _("More than 3 months, less than 1 year")),
#     ("morethan1y", _("More than 1 year ago")),
# ]

med_cond_opt = (
        ("none", _("None")),
        ("asthma", _("Asthma")),
        ("cystic", _("Cystic Fibrosis")),
        ("copd", _("COPD/Emphysema")),
        ("pulmonary", _("Pulmonary Fibrosis")),
        ("lung", _("Other lung diseases")),
        ("hbp", _("High Blood Pressure")),
        ("angina", _("Angina")),
        ("stroke", _("Previous Stroke or Transient ischemic attack")),
        ("heartattack", _("Previous heart attack")),
        ("valvular", _("Valvular heart disease")),
        ("other", _("Other heart disease")),
        ("diabetes", _("Diabetes")),
        ("cancer", _("Cancer")),
        ("organ", _("Previous organ transplant")),
        ("hiv", _("HIV or impaired immune system")),
        ("longterm", _("Other long-term condition")),
    )

symptoms_opt = (
        ("none", _("None")),
        ("fever", _("Fever (feeling feverish or warmer than usual)")),
        ("chills", _("Chills")),
        ("drycough", _("Dry cough")),
        ("wetcough", _("Wet cough")),
        ("difficultbreath", _("Difficult breathing or feeling shortness of breath")),
        ("chestpain", _("Chest pain")),
        ("losstastesmell", _("Loss of taste or smell")),
        ("confusion", _("Confusion")),
        ("dizzy", _("Dizziness or vertigo")),
        ("headache", _("Headache")),
        ("muscleache", _("Muscle aches")),
        ("sorethroat", _("Sore throat, runny and blocked nose")),
    )

# Create your models here.
class questionnairedata(models.Model):
    questionid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    respondent_choices = models.CharField(max_length = 50, choices=respondent_choices, default='', verbose_name=_('1. Which group of respondents you are?'))
    respondent_sex = models.CharField(max_length=50, choices=respondent_sex, default='', verbose_name=_('2. What is your biological sex?'))
    age = models.IntegerField(verbose_name=_('How old are you?'))
    med_cond_opt = MultiSelectField(choices=med_cond_opt, default=False, verbose_name=_('3. Do you have any of these medical conditions? (can choose more than one)'))
    respondent_smoke = MultiSelectField(choices=respondent_smoke, default=False, verbose_name=_('4. Do you, or have you, ever smoked (including e-cigarettes)?'))
    symptoms_opt = MultiSelectField(choices=symptoms_opt, default=False, verbose_name=_('5. Do you have the following symptoms irrespective of having confirmed with COVID-19 or not? (can choose more than one)'))
    date_diagnosed = models.DateField (blank=True,null=True,default=None,verbose_name=_('When was you being diagnosed for that infection? '))
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True)
    vaccinated = models.CharField(max_length=50,choices=respondent_vaccine,default='', verbose_name=_('Have Vaccinated?')) 
    date_vaccinated = models.DateField(blank=True, null=True, default=None, verbose_name=_('Date vaccinated'))
    date_created = models.DateTimeField(auto_now_add=True)  

    
from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
import uuid

respondent_choices = [
    ("healthy", "Healthy individual"),
    ("positive", "COVID-19 (currently positive)"),
    ("tuberculosis", "Tuberculosis"),
    ("pnuemonia", "Pnuemonia (not due to COVID-19)"),

]

respondent_sex = [
    ('male', 'Male'),
    ('female', 'Female'),
]

respondent_smoke = [
    ("never", "Never smoked"),
    ("exsmoker", "Ex-smoker"),
    ("current1", "Current smoker (less than one a day)"),
    ("current2", "Current smoker (1 to 10 cigarettes per day)"),
    ("current3", "Current smoker (11 to 20 cigarettes per day)"),
    ("current4", "Current smoker (21+ cigarettes per day)"),
    ("current5", "Current smoker (e-cigarettes only)"),
]

date_diagnosed = [
    ("last14days", "Within last 14 days"),
    ("morethan14days", "More than 14 days ago, less than 3 months"),
    ("morethan3m", "More than 3 months, less than 1 year"),
    ("morethan1y", "More than 1 year ago"),
]

med_cond_opt = (
        ("none", "None"),
        ("asthma", "Asthma"),
        ("cystic", "Cystic Fibrosis"),
        ("copd", "COPD/Emphysema"),
        ("pulmonary", "Pulmonary Fibrosis"),
        ("lung", "Other lung diseases"),
        ("hbp", "High Blood Pressure"),
        ("angina", "Angina"),
        ("stroke", "Previous Stroke or Transient ischemic attack"),
        ("heartattack", "Previous heart attack"),
        ("valvular", "Valvular heart disease"),
        ("other", "Other heart disease"),
        ("diabetes", "Diabetes"),
        ("cancer", "Cancer"),
        ("organ", "Previous organ transplant"),
        ("hiv", "HIV or impaired immune system"),
        ("longterm", "Other long-term condition"),
    )

symptoms_opt = (
        ("none", "None"),
        ("fever", "Fever (feeling feverish or warmer than usual)"),
        ("chills", "Chills"),
        ("drycough", "Dry cough"),
        ("wetcough", "Wet cough"),
        ("difficultbreath", "Difficult breathing or feeling shortness of breath"),
        ("chestpain", "Chest pain"),
        ("losstastesmell", "Loss of taste or smell"),
        ("confusion", "Confusion"),
        ("dizzy", "Dizziness or vertigo"),
        ("headache", "Headache"),
        ("muscleache", "Muscle aches"),
        ("sorethroat", "Sore throat, runny and blocked nose"),
    )

# Create your models here.
class questionnairedata(models.Model):
    questionid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False, unique=True)
    respondent_choices = models.CharField(max_length = 50, choices=respondent_choices, default='', verbose_name='Which group of respondents you are?')
    respondent_sex = models.CharField(max_length=50, choices=respondent_sex, default='', verbose_name=' What is your biological sex?')
    age = models.IntegerField(verbose_name='How old are you?')
    med_cond_opt = MultiSelectField(choices=med_cond_opt, default=False, verbose_name=' Do you have any of these medical conditions? (can choose more than one)')
    respondent_smoke = models.CharField(max_length=100, choices=respondent_smoke, default='', verbose_name='Do you, or have you, ever smoked (including e-cigarettes)?')
    symptoms_opt = MultiSelectField(choices=symptoms_opt, default=False, verbose_name='Do you have the following symptoms irrespective of having confirmed with COVID-19 or not? (can choose more than one)')
    date_diagnosed = models.CharField(max_length=100, choices=date_diagnosed, default='', verbose_name='When was you being diagnosed for that infection? ')

class Cough(models.Model):
    cough_id = models.UUIDField(primary_key=True, default=uuid.uuid4(),editable=False,unique=True)
    cough_record = models.FileField()
    
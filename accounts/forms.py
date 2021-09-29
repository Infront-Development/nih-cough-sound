from django import forms
from django.contrib.auth import models
from accounts.models import Subjects


class registerSubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('subjects_phone_number',)

class loginSubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('subjects_login','subjects_phone_number',)
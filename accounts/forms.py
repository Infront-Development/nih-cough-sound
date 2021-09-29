from django import forms
from django.contrib.auth import models
from accounts.models import Subjects


class registerSubjectsForm(forms.ModelForm):
    subjects_phone_number = forms.CharField(label="Please Input your Phone Number")

    class Meta:
        model = Subjects
        fields = ('subjects_phone_number',)

class loginSubjectsForm(forms.ModelForm):
    subjects_login = forms.CharField(label="User ID ")
    subjects_phone_number = forms.CharField(label="Phone Number :")

    class Meta:
        model = Subjects
        fields = ('subjects_login','subjects_phone_number',)
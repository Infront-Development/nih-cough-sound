from django import forms
from django.contrib.auth import models
from accounts.models import Subjects
from django.forms import ValidationError

class registerSubjectsForm(forms.ModelForm):
    subjects_phone_number = forms.CharField(label="Please Input your Phone Number")

    class Meta:
        model = Subjects
        fields = ('subjects_phone_number',)

class loginSubjectsForm(forms.ModelForm):
    subjects_login = forms.CharField(label="User ID ")

    class Meta:
        model = Subjects
        fields = ('subjects_login',)

    def clean_subject_login(self):
        data  = self.cleaned_data
        subject_login = data["subject_login"]
        if not Subjects.objects.filter(subjects_login=subject_login).exists():
            raise ValidationError("ID DOES NOT EXISTS")
        return subject_login
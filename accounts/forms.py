from django import forms
from django.contrib.auth import models
from accounts.models import Subjects
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _, ugettext_lazy 


class RegisterSubjectForm(forms.ModelForm):
    phone_number = forms.CharField(label=_("Please input your Phone Number"))

    class Meta:
        model = Subjects
        fields = ('phone_number',)

class LoginSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ('phone_number',)

    def clean_phone_number(self):
        data  = self.cleaned_data
        phone_number = data["phone_number"]
        if not Subjects.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(_("PHONE NUMBER DOES NOT EXIST"))
        return phone_number
from django import forms
from .models import feedback
from django.utils.translation import gettext_lazy as _

rating_choice = (
    ("1", '1'),
    ("2", '2'),
    ("3", '3'),
    ("4", '4'),
    ("5", '5'),
)

class feedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=rating_choice,
        widget=forms.RadioSelect(),
        label=_("Rating")
        )
    
    class Meta:
        model = feedback
        fields = ('rating','remarks')
        

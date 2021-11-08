from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Fieldset, Layout, HTML,Div
from django.core import validators
from questionnaire.models import questionnairedata
import datetime
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
class questionnaire(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


        self.helper.form_tag = False    

        self.helper.layout = Layout(
            'vaccinated',
            Field('date_vaccinated', style="width : 200px"),
            'respondent_choices',
            Field('date_diagnosed',style="width : 200px"),
            'respondent_sex',
            Div(Field('age', style="width : 150px"), 
            HTML(str(_(r"<span class='text-danger'>*Disclaimer : Your data will not be collected if you are under 18 year old</span>")))),
            'med_cond_opt',
            Field('respondent_smoke'),
            'symptoms_opt'
        )
    class Meta: 
        model = questionnairedata
        fields = ('respondent_choices','date_diagnosed', 'respondent_sex', 'age', 'med_cond_opt', 'respondent_smoke', 'symptoms_opt', 'vaccinated','date_vaccinated' )
        widgets = {'respondent_choices':forms.RadioSelect,'respondent_sex':forms.RadioSelect,
                    'respondent_smoke':forms.CheckboxSelectMultiple,'vaccinated':forms.RadioSelect,'date_diagnosed':forms.DateInput(attrs={'type': 'date','disabled':'True'}),
                    'med_cond_opt':forms.CheckboxSelectMultiple, 'symptoms_opt':forms.CheckboxSelectMultiple,
                    'date_vaccinated' : forms.DateInput(attrs={'type' : 'date','disabled':'True'})
                    }
    
      
    def clean_med_cond_opt(self):
        med_cond_opt = self.cleaned_data["med_cond_opt"]
        if 'none' in med_cond_opt:
            med_cond_opt.clear() # Clear all optiosn 
            med_cond_opt.append('none') # re-append none 

        return med_cond_opt

    

        

    def clean_symptoms_opt(self):
        symptopms_opt = self.cleaned_data["symptoms_opt"]
        if 'none' in symptopms_opt:
            symptopms_opt.clear() # Clear all optiosn 
            symptopms_opt.append('none') # re-append none 

        return symptopms_opt

    def clean_date_vaccinated(self):
        vaccinated = self.cleaned_data['vaccinated']
        date_vaccinated = self.cleaned_data['date_vaccinated']
        if not vaccinated and date_vaccinated:
            date_vaccinated = None
        return date_vaccinated

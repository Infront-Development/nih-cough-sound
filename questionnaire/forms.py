from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Fieldset, Layout
from questionnaire.models import questionnairedata

class questionnaire(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


        self.helper.form_tag = False    

        self.helper.layout = Layout(
            'respondent_choices',
            'date_diagnosed',
            'respondent_sex',
            'age',
            'med_cond_opt',
            Field('respondent_smoke'),
            'symptoms_opt'
        )
    class Meta: 
        model = questionnairedata
        fields = ('respondent_choices','date_diagnosed', 'respondent_sex', 'age', 'med_cond_opt', 'respondent_smoke', 'symptoms_opt', )
        widgets = {'respondent_choices':forms.RadioSelect,'respondent_sex':forms.RadioSelect,
                    'respondent_smoke':forms.Select, 'date_diagnosed':forms.RadioSelect,
                    'med_cond_opt':forms.CheckboxSelectMultiple, 'symptoms_opt':forms.CheckboxSelectMultiple}
    
      
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
  

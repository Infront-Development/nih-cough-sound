from django import forms
from questionnaire.models import questionnairedata

class questionnaire(forms.ModelForm):
    class Meta: 
        model = questionnairedata
        fields = ('respondent_choices', 'respondent_sex', 'age', 'med_cond_opt', 'respondent_smoke', 'symptoms_opt', 'date_diagnosed')
        widgets = {'respondent_choices':forms.RadioSelect,'respondent_sex':forms.RadioSelect, 'respondent_smoke':forms.RadioSelect, 'date_diagnosed':forms.RadioSelect, 'med_cond_opt':forms.CheckboxSelectMultiple, 'symptoms_opt':forms.CheckboxSelectMultiple}
    


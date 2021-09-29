from django import forms
from django.db.models import fields
from django.forms import widgets
from subjects.models import questionnairedata
from accounts.models import Subjects

class questionnaire(forms.ModelForm):
    class Meta: 
        model = questionnairedata
        fields = ('respondent_choices', 'respondent_sex', 'age', 'med_cond_opt', 'respondent_smoke', 'symptoms_opt', 'date_diagnosed')
        widgets = {'respondent_choices':forms.RadioSelect,'respondent_sex':forms.RadioSelect, 'respondent_smoke':forms.RadioSelect, 'date_diagnosed':forms.RadioSelect, 'med_cond_opt':forms.CheckboxSelectMultiple, 'symptoms_opt':forms.CheckboxSelectMultiple}
    
class questform(forms.Form):

    def __init__(self, *args, **kwargs):
        super(questform, self).__init__(*args, **kwargs)
        self.fields['respondent_choices'].label= 'Which group of respondents you are?'

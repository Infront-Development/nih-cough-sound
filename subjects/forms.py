from django import forms
from django.db.models import fields
from django.forms import widgets
from subjects.models import questionnairedata



class questionnaire(forms.ModelForm):
    # respondent_choices = forms.CharField(label = 'Which group of respondents you are?', widget=forms.RadioSelect())
    # respondent_sex = forms.CharField(label = 'What is your biological sex?', widget=forms.RadioSelect())
    # age = forms.IntegerField(label = "How old are you?")
   
    # med_cond_opt = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)
    # respondent_smoke = forms.CharField(label = 'Do you, or have you, ever smoked (including e-cigarettes)?', widget = forms.RadioSelect())
   
    # symptoms_opt = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)
    # date_diagnosed = forms.CharField(label = 'When was you being diagnosed for that infection?', widget = forms.Select())

    class Meta: 
        model = questionnairedata
        fields = ('respondent_choices', 'respondent_sex', 'age', 'med_cond_opt', 'respondent_smoke', 'symptoms_opt', 'date_diagnosed')
        widgets = {'respondent_choices':forms.RadioSelect,'respondent_sex':forms.RadioSelect, 'respondent_smoke':forms.RadioSelect, 'date_diagnosed':forms.RadioSelect, 'med_cond_opt':forms.CheckboxSelectMultiple, 'symptoms_opt':forms.CheckboxSelectMultiple}
        

class questform(forms.Form):
    # respondent_choices = forms.CharField(widget=forms.RadioSelect())
    # respondent_sex = forms.CharField(widget=forms.RadioSelect())
    # age = forms.IntegerField()
   
    # questionnaire = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)
    # respondent_smoke = forms.CharField(widget = forms.RadioSelect())
   
    # questionnaire = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)
    # questionnaire = forms.CharField(widget = forms.Select())

    def __init__(self, *args, **kwargs):
        super(questform, self).__init__(*args, **kwargs)
        self.fields['respondent_choices'].label= 'Which group of respondents you are?'


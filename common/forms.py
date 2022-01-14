from django import forms
from .models import feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field,Layout
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class feedbackForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_tag = False    
        self.helper.layout = Layout(
            "rating",
            'remarks'
        )
    
    
    class Meta:
        model = feedback
        fields = ('rating','remarks')
        widgets = {'rating':forms.RadioSelect,'remarks':forms.Textarea}
        
    
        

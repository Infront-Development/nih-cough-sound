
from django.shortcuts import render
from django.utils.translation import gettext as _



# Create your views here.
def consent(request):
    return render(request, 'consent-pop-up.html')

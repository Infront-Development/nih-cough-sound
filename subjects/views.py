from subjects.models import questionnairedata
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from subjects.forms import questionnaire
from subjects.models import Cough
import ssl
import cgi
import wave
import contextlib

# Create your views here.
def consent(request):
    return render(request, 'consent-pop-up.html')

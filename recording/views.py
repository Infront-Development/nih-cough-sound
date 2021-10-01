from re import sub
from typing import Sized
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.checks import messages
from django.shortcuts import render
from django.utils.translation import gettext as _
from recording.models import Cough,Breath
from accounts.models import Subjects
# Create your views here.

def record(request):
    subject_id = request.session['subject_login']
    subject_details = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        audio = request.FILES.get('audio_data')
        record = Cough(cough_record=audio,subjects=subject_details)
        record.save()
    else:
        context = {
        'id': request.session['subject_login']
        }
        return render(request,'consent-pop-up.html',context)

def breathPage(request):
    subject_id = request.session['subject_login']
    subject_details = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        print("im here")
        audio = request.FILES.get('audio_data')
        record = Breath(breath_record=audio,subjects=subject_details)
        record.save()
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"breath.html",context)

def viewRecording(request):
    cough = Cough.objects.all()
    print("got data")
    context = {
        'cough': cough,
        'title': "Cough"
    }
    return render(request,'record.html',context)

def viewBreathRecording(request):
    context = {
        'title': "Breathing"
    }
    return render(request,'record.html',context)

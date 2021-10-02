from re import sub
from typing import Sized
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.checks import messages
from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.translation import gettext as _
from recording.models import Cough,Breath
from accounts.models import Subjects
# Create your views here.

def record(request):
    subject_id = request.session['subject_login']
    subject_details = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        audios = request.FILES.getlist('audio_data')
        
        records = []
        for audio in audios:
            records.append(Cough(cough_record=audio,subjects=subject_details))
        
        Cough.objects.bulk_create(records)
        return JsonResponse({"STATUS" : "SUCCESS"})
    else:
        context = {
        'id': request.session['subject_login']
        }
        return render(request,'consent-pop-up.html',context)

def breathPage(request):
    subject_id = request.session['subject_login']
    subject_details = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        audios = request.FILES.getlist('audio_data')
        records = []
        for audio in audios:
            Breath.append(Cough(cough_record=audio,subjects=subject_details))
        Breath.objects.bulk_create(records)
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"breath.html", context)

def viewRecording(request):
    cough = Cough.objects.all()
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

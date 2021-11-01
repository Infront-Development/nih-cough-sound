from re import sub
from typing import Sized
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.checks import messages
from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.translation import gettext as _
from django.db.models import F, Value
from django.db.models.functions import Concat
from recording.models import AudioRecordSample
from accounts.models import Subjects

from django.shortcuts import HttpResponseRedirect
# Create your views here.

def consent_page(request):
    context = {
        'id': request.session['subject_login']
        }
    return render(request,'recording/consent-pop-up.html',context)

def cough_page(request):
    if 'subject_login' not in request.session:
        return HttpResponseRedirect('/')
    subject_id = request.session['subject_login']
    subject = Subjects.objects.get(phone_number=subject_id)
    if request.is_ajax():
        audio_mask = request.FILES.getlist('audio_data_mask')
        audio_no_mask = request.FILES.getlist('audio_data_no_mask')
        
        if not (len(audio_mask) == 2 and len(audio_no_mask) == 2):
            return JsonResponse({
                "status" : "Fail",
                "msg" : "Must send 3 audios!"   
            })
        else:
            recording_sample = AudioRecordSample(
                subjects=subject,
                audio1=audio_no_mask[0],
                audio2=audio_no_mask[1],
                audio3=audio_mask[0],
                audio4=audio_mask[1],
                sound_type="cough"
            )

            recording_sample.save() 
        return JsonResponse({"status" : "Success"})
    else:
        context = {
        'id': request.session['subject_login']
        }
        return render(request,'recording/cough.html',context)

def breath_page(request):

    if 'subject_login' not in request.session:
        return HttpResponseRedirect('/')
    subject_id = request.session['subject_login']
    subject = Subjects.objects.get(phone_number=subject_id)
    if request.is_ajax():
        audio_mask = request.FILES.getlist('audio_data_mask')
        audio_no_mask = request.FILES.getlist('audio_data_no_mask')
        
        if not (len(audio_mask) == 2 and len(audio_no_mask) == 2):
            return JsonResponse({
                "status" : "Fail",
                "msg" : "Must send 3 audios!"   
            })
        else:
            recording_sample = AudioRecordSample(
                subjects=subject,
                audio1=audio_no_mask[0],
                audio2=audio_no_mask[1],
                audio3=audio_mask[0],
                audio4=audio_mask[1],
                sound_type="cough"
            )

            recording_sample.save() 
        return JsonResponse({"status" : "Success"})
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"recording/breath.html", context)

def view_cough_recording(request):
    audio_samples = AudioRecordSample.objects.select_related('subjects')
    context = {
        'audio_samples': audio_samples,
        'title': "Cough"
    }
    return render(request,'recording/record.html',context)

def view_breath_recording(request):
    context = {
        'title': "Breathing"
    }
    return render(request,'recording/record.html',context)

from re import sub
from typing import Sized
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.checks import messages
from django.shortcuts import render
from django.http.response import JsonResponse
from django.utils.translation import gettext as _
from recording.models import AudioRecordSample
from accounts.models import Subjects
# Create your views here.

def record(request):
    subject_id = request.session['subject_login']
    subject = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        audios = request.FILES.getlist('audio_data')
        
        if len(audios) != 3:
            return JsonResponse({
                "status" : "Fail",
                "msg" : "Must send 3 audios!"
            })
        else:
            recording_sample = AudioRecordSample(
                subjects=subject,
                audio1=audios[0],
                audio2=audios[1],
                audio3=audios[2],
                sound_type="cough"
            )

            recording_sample.save()
        return JsonResponse({"STATUS" : "SUCCESS"})
    else:
        context = {
        'id': request.session['subject_login']
        }
        return render(request,'consent-pop-up.html',context)

def breathPage(request):
    subject_id = request.session['subject_login']
    subject = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        audios = request.FILES.getlist('audio_data')
        
        if len(audios) != 3:
            return JsonResponse({
                "status" : "Fail",
                "msg" : "Must send 3 audios!"
            })
        else:
            recording_sample = AudioRecordSample(
                subjects=subject,
                audio1=audios[0],
                audio2=audios[1],
                audio3=audios[2],
                sound_type="breath"
            )

            recording_sample.save()
        return JsonResponse({"STATUS" : "SUCCESS"})
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"breath.html", context)

def viewRecording(request):
    audio_samples = AudioRecordSample.objects.select_related('subjects')
    context = {
        'audio_samples': audio_samples,
        'title': "Cough"
    }
    return render(request,'record.html',context)

def viewBreathRecording(request):
    context = {
        'title': "Breathing"
    }
    return render(request,'record.html',context)

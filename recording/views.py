from django.shortcuts import render
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from recording.models import AudioRecordSample, AudioRecord
from accounts.models import Subject
from result.models import DiagnoseResult
from django.utils import timezone

from common.decorators import require_subject_login, must_agree_consent,cooldown

from asgiref.sync import sync_to_async, async_to_sync

import asyncio
import json
import requests
from threading import Thread

from .tasks import predict

@must_agree_consent
@require_subject_login
@cooldown
def record_main(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login'],
            'title' : "Cough Sound Project | Record Home",
        }

        # Set cough taken flag which is used to track whether the user has recorded cough sound or not
        if "cough_taken" not in request.session:
            request.session['cough_taken'] = False 
        return render(request, "recording/part-1-menu.html", context)


@must_agree_consent
@require_subject_login
@cooldown
def cough_with_mask_page(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
    if request.method == "POST":
        audios = request.FILES.getlist('audio[]')

        if len(audios) < 2:
            return JsonResponse({
                "status" : 0,
                "reason" : "Must Send 2 Audio ! "
            }) 
        
        samples = AudioRecordSample(
            subject=subject,   
            audio1=audios[0],
            audio2=audios[1],
            sound_type="cough",
        )

        samples.save()

        return JsonResponse(
            {
                "status" : 1,
                "reason" : "Audio Cough Part 1 is saved"
            })
    else:
        context = {
        'id': request.session['subject_login'],
        'next_page' : reverse_lazy("recording:cough_part_2"),
        'language':request.LANGUAGE_CODE,
        'title': "Cof'e | Record Cough with Mask"
        }
        return render(request,'recording/cough/cough-with-mask.html',context)
        
@must_agree_consent
@require_subject_login
@cooldown
def cough_no_mask_page(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
    if request.method == "POST":
        audio_files = request.FILES.getlist('audio[]')

        if len(audio_files) < 2:
            return JsonResponse({
               "status" : 0,
                "reason" : "Must Send 2 Audio ! "
            }) 

        try:
            samples = subject.audiorecordsample_set.filter(sound_type="cough").latest('upload_time')
        except AudioRecordSample.DoesNotExist:
            return JsonResponse(
                {
                    "status" : 0,
                    "reason" : "Must complete first part of recording"
                }
            ) 
        
        samples.audio3 = audio_files[0]
        samples.audio4 = audio_files[1]
        samples.save()
        return JsonResponse(
            {
                "status" : 1,
                "reason" : "You Completed recording for cough page !"
            }
        )
    else:
        context = {
            'id': request.session['subject_login'],
            'next_page' : reverse_lazy("recording:instruction_breath"),
            'language':request.LANGUAGE_CODE,
            'title': "Cof'e | Record Cough with No Mask"
        }
        return render(request,'recording/cough/cough-no-mask.html',context)
    


@must_agree_consent
@require_subject_login
@cooldown
def breath_no_mask_page(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
    if request.method == "POST":
        audio_files = request.FILES.getlist('audio[]')

        if len(audio_files) < 2:
            return JsonResponse({
               "status" : 0,
                "reason" : "Must Send 2 Audio ! "
            }) 

        try:
            samples = subject.audiorecordsample_set.filter(sound_type="breath").latest('upload_time')
        except AudioRecordSample.DoesNotExist:
            return JsonResponse(
                {
                    "status" : 0,
                    "reason" : "Must complete first part of recording"
                }
            ) 
        
        samples.audio3 = audio_files[0]
        samples.audio4 = audio_files[1]
        samples.save()
        return JsonResponse(
            {
                "status" : 1,
                "reason" : "You Completed recording for cough page !"
            }
        )
    else:
        context = {
            'id': request.session['subject_login'],
            'next_page' :  reverse_lazy("common:feedback_subject"),
            'language':request.LANGUAGE_CODE,
            'title': "Cof'e | Record Breath with No Mask"
        }
        return render(request,"recording/breath/breath-no-mask.html", context)

@must_agree_consent
@require_subject_login
def breath_with_mask_page(request):

    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
    if request.method == "POST":
        audios = request.FILES.getlist('audio[]')

        if len(audios) < 2:
            return JsonResponse({
                "status" : 0,
                "reason" : "Must Send 2 Audio ! "
            }) 
        
        samples = AudioRecordSample(
            subject=subject,   
            audio1=audios[0],
            audio2=audios[1],
            sound_type="breath",
        )

        samples.save()
        
        

        return JsonResponse(
            {"status" : 1,
            
            })
    else:
        context = {
            'id': request.session['subject_login'],
            'next_page' :  reverse_lazy("recording:breath_part_2"),
            'language':request.LANGUAGE_CODE,
            'title': "Cof'e | Record Breath with Mask"
        }
        
        return render(request,"recording/breath/breath-with-mask.html", context)


def view_cough_recording(request):
    audio_samples = AudioRecordSample.objects.select_related('subject')
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


@require_subject_login
@must_agree_consent
def instruc_page(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        return render(request, "recording/instruc.html", context)
    
    
@require_subject_login
@must_agree_consent
def instruction_cough(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        
        return render(request, "recording/instruc-cough.html", context)

@require_subject_login
@must_agree_consent
def instruc_breath_page(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        return render(request, "recording/instruc-breath.html", context)

@must_agree_consent
@require_subject_login
@cooldown
def record_cough(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
    if request.method == "POST":
        audios = request.FILES.getlist('audio[]')
        if len(audios) < 1:
            return JsonResponse({
                "status" : 0,
                "reason" : "Must Send Audio!"
            }) 
        
        samples = AudioRecord(
            subject=subject,   
            audio=audios[0],
            sound_type="cough",
        )

        samples.save()

        # Analyze audio
        # analyze_cough = Thread(
        #     target=predict(subject_id, audios[0], subject),
        #     daemon=True
        # )
        # analyze_cough.start()
        # analyze_cough = predict.now(subject_id, audios[0], subject)
        # analyze_cough = asyncio.run(predict(subject_id, audios[0], subject))
        # predict(subject_id, audios[0], subject)
        predict.delay.apply_async(phone_number=subject_id, audio_file=audios[0], subject=subject)

        return JsonResponse(
            {
                "status" : 1,
                "reason" : "Audio Cough is saved"
            })
    else:
        context = {
        'id': request.session['subject_login'],
        'next_page' : reverse_lazy('questionnaire:questionnaire_form'),
        'language':request.LANGUAGE_CODE,
        'title': "Cof'e | Record Cough"
        }
        return render(request,'recording/cough/cough-new.html',context)
        
       
# def instruc_page(request):
#     data= request.POST.get('instruc_page')
#     context= {'data':data}
#     return render(request, 'recording/cough.html', context)
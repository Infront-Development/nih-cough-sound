from django.shortcuts import render
from django.http.response import JsonResponse
from recording.models import AudioRecordSample
from accounts.models import Subject

from common.decorators import require_subject_login, must_agree_consent
# Create your views here.


@must_agree_consent
@require_subject_login
def record_main(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login'],
            'title' : "Cough Sound Project | Record Home",
        }
        if "cough_taken" not in request.session:
            request.session['cough_taken'] = True
        return render(request, "recording/part-1-menu.html", context)

@must_agree_consent
@require_subject_login
def cough_page(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
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
                subject=subject,
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

@must_agree_consent
@require_subject_login
def cough_no_mask_page(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
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
                subject=subject,
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
        return render(request,'recording/cough-no-mask.html',context)
    

@must_agree_consent
@require_subject_login
def cough_with_mask_page(request):
    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
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
                subject=subject,
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
        return render(request,'recording/cough-with-mask.html',context)


@must_agree_consent
@require_subject_login
def breath_page(request):

    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
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
                subject=subject,
                audio1=audio_no_mask[0],
                audio2=audio_no_mask[1],
                audio3=audio_mask[0],
                audio4=audio_mask[1],
                sound_type="breath"
            )

            recording_sample.save() 
        return JsonResponse({"status" : "Success"})
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"recording/breath.html", context)

@must_agree_consent
@require_subject_login
def breath_no_mask_page(request):

    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
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
                subject=subject,
                audio1=audio_no_mask[0],
                audio2=audio_no_mask[1],
                audio3=audio_mask[0],
                audio4=audio_mask[1],
                sound_type="breath"
            )

            recording_sample.save() 
        return JsonResponse({"status" : "Success"})
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"recording/breath-no-mask.html", context)

@must_agree_consent
@require_subject_login
def breath_with_mask_page(request):

    subject_id = request.session['subject_login']
    subject = Subject.objects.get(phone_number=subject_id)
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
                subject=subject,
                audio1=audio_no_mask[0],
                audio2=audio_no_mask[1],
                audio3=audio_mask[0],
                audio4=audio_mask[1],
                sound_type="breath"
            )

            recording_sample.save() 
        return JsonResponse({"status" : "Success"})
    else:
        context = {
            'id': request.session['subject_login']
        }
        return render(request,"recording/breath-with-mask.html", context)


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


def instruc_page(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        return render(request, "recording/instruc.html", context)
    
    
def instruction_cough(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        
        return render(request, "recording/instruc-cough.html", context)

def instruc_breath_page(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        return render(request, "recording/instruc-breath.html", context)




       
# def instruc_page(request):
#     data= request.POST.get('instruc_page')
#     context= {'data':data}
#     return render(request, 'recording/cough.html', context)
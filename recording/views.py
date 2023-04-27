from django.shortcuts import render
from django.http.response import JsonResponse
from django.urls import reverse_lazy
from recording.models import AudioRecordSample, AudioRecord
from accounts.models import Subject

from common.decorators import require_subject_login, must_agree_consent, cooldown


@must_agree_consent
@require_subject_login
@cooldown
def record_main(request):
    if request.method == "GET":
        context = {
            'id': request.session['subject_login'],
            'title': "Cough Sound Project | Record Home",
        }

        # Set cough taken flag which is used to track whether the user has recorded cough sound or not
        if "cough_taken" not in request.session:
            request.session['cough_taken'] = False
        return render(request, "recording/part-1-menu.html", context)






def view_cough_recording(request):
    audio_samples = AudioRecordSample.objects.select_related('subject')
    context = {
        'audio_samples': audio_samples,
        'title': "Cough"
    }
    return render(request, 'recording/record.html', context)


def view_breath_recording(request):
    context = {
        'title': "Breathing"
    }
    return render(request, 'recording/record.html', context)


@require_subject_login
@must_agree_consent
def instruc_page(request):
    if request.method == "GET":
        context = {
            'id': request.session['subject_login']
        }
        return render(request, "recording/instruc.html", context)


@require_subject_login
@must_agree_consent
def instruction_cough(request):
    if request.method == "GET":
        context = {
            'id': request.session['subject_login']
        }

        return render(request, "recording/instruc-cough.html", context)


@require_subject_login
@must_agree_consent
def contribute_page(request):
    return render(request, "contribute_option.html")

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
                "status": 0,
                "reason": "Must Send Audio!"
            })

        samples = AudioRecord(
            subject=subject,
            audio=audios[0],
            sound_type="cough",
        )

        samples.save()

        return JsonResponse(
            {
                "status": 1,
                "reason": "Audio Cough is saved"
            })
    else:
        if request.session.get('activity') == 'tuberculosis-contribute':
            next_page = reverse_lazy(
                'questionnaire:tuberculosis-contribute-form')
            category = "tuberculosis"
        elif request.session.get('activity') == 'covid-contribute':
            next_page = reverse_lazy(
                'questionnaire:covid-contrib-contribute-form')
            category = "covid-19"
        else:
            next_page = reverse_lazy('questionnaire:questionnaire_form')
            category = "prediction"

        context = {
            'id': request.session['subject_login'],
            'next_page': next_page,
            'category': category,
            'language': request.LANGUAGE_CODE,
            'title': "Cof'e | Record Cough"
        }
        return render(request, 'recording/cough/cough-new.html', context)


# def instruc_page(request):
#     data= request.POST.get('instruc_page')
#     context= {'data':data}
#     return render(request, 'recording/cough.html', context)

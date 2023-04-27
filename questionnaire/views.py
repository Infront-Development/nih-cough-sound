from django.contrib import messages
from django.shortcuts import redirect, render
from api.external import send_to_aws
from questionnaire.forms import questionnaire
from questionnaire.models import QuestionnaireData
from accounts.models import Subject
from datetime import datetime, timedelta
from common.decorators import require_subject_login, must_agree_consent, cooldown
from result.models import DiagnoseResult
from django.db import transaction

from recording.models import AudioRecord
from django.utils import timezone

import json
import requests

API_ENDPOINT_URL = "http://cough.swincloud.com/api/covid_detect"
UPLOAD_ENDPOINT_URL = "https://kxn3fbykyd.execute-api.ap-southeast-1.amazonaws.com/v1/coughsound/%7Bfilename%7D"


def predict(subject_id, audio, subject):
    print("Analyzing")

    headers = {}
    cough_mp3 = audio.open(mode='rb')
    files = {
        "file": ('cough.wav', cough_mp3, 'audio/wav')
    }
    r = requests.request("POST", API_ENDPOINT_URL,
                         headers=headers, files=files).text
    status = json.loads(r)["message"]
    if status == "":
        status = "Invalid"

    response = {
        "covid_status": status,
        "confidence_rate": 18,
        "phone_number": subject_id,
        "subject": subject,
        "date_created": timezone.now()
    }

    DiagnoseResult.objects.create(**response)


# create questionnaire data
@require_subject_login
@must_agree_consent
@cooldown
def questionnaire_form(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subject.objects.get(
            phone_number=request.session['subject_login'])
        if form.is_valid():
            questionnaire_: QuestionnaireData = form.save(commit=False)

            # Do not proceed if participatn is below 18 year old
            if not questionnaire_.is_eligible:
                messages.success(
                    request, "Thank you for participating in Cof'e. However, the data you send will not be submitted as you are below 18 year old")
                return redirect("common:thankyou_subject")

            with transaction.atomic():
                questionnaire_.subject = subject
                questionnaire_.save()

                subject.reset_cooldown()
                subject.save()

                audio_record = AudioRecord.objects\
                                          .filter(subject=subject)\
                                          .order_by("-upload_time")\
                                          .first()

                buffer, filename = audio_record.aws_file

                response = send_to_aws(buffer, filename)
                if response.status_code != 200:
                    messages.error(
                        request, "Please re-fill the questionnaire and try-again")
                    return render(request, "questionnaire/questionnaire.html", {'form': form, 'title': "Questionnaire"})

                return redirect('common:thankyou_subject')
        else:
            messages.error(
                request, "Please re-fill the questionnaire and try-again")
            return render(request, "questionnaire/questionnaire.html", {'form': form, 'title': "Questionnaire"})
    else:
        form = questionnaire()
        return render(request, "questionnaire/questionnaire.html", {'form': form, 'title': "Questionnaire"})

# to view the questionnaire list


@require_subject_login
@must_agree_consent
@cooldown
def view_questionnaire_list(request):
    allforms = QuestionnaireData.objects.all()
    context = {'allforms': allforms}
    return render(request, 'formlist.html', context)


def thank_subject(request):
    context = {
        'id': request.session['subject_login'],
        'title': 'Cough Sound Project | Thank you for your participant',
    }
    return render(request, 'questionnaire/thanks_user.html', context)


def tuberculosis_questionnaire_form(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subject.objects.get(
            phone_number=request.session['subject_login'])
        if form.is_valid():
            questionnaire_: QuestionnaireData = form.save(commit=False)

            request.session['activity'] = "cough-test"

            # Do not proceed if participatn is below 18 year old
            if not questionnaire_.is_eligible:
                messages.success(
                    request, "Thank you for participating in Cof'e. However, the data you send will not be submitted as you are below 18 year old")
                return redirect("common:thankyou_subject")

            with transaction.atomic():
                questionnaire_.subject = subject
                questionnaire_.save()

                subject.reset_cooldown()
                subject.save()

                audio_record = AudioRecord.objects\
                                          .filter(subject=subject)\
                                          .order_by("-upload_time")\
                                          .first()

                buffer, filename = audio_record.aws_file

                response = send_to_aws(buffer, filename)
                if response.status_code != 200:
                    messages.error(
                        request, "Please re-fill the questionnaire and try-again")
                    return render(request, "questionnaire/tuberculosis_quetionnaire.html", {'form': form, 'title': "Questionnaire"})

                return redirect('common:thankyou_subject')
        else:
            messages.error(
                request, "Please re-fill the questionnaire and try-again")
            return render(request, "questionnaire/tuberculosis_quetionnaire.html", {'form': form, 'title': "Questionnaire"})
    else:
        form = questionnaire()
        return render(request, "questionnaire/tuberculosis_quetionnaire.html", {'form': form, 'title': "Questionnaire"})


def covid_contrib_questionnaire_form(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subject.objects.get(
            phone_number=request.session['subject_login'])
        if form.is_valid():
            questionnaire_: QuestionnaireData = form.save(commit=False)

            request.session['activity'] = "cough-test"

            # Do not proceed if participatn is below 18 year old
            if not questionnaire_.is_eligible:
                messages.success(
                    request, "Thank you for participating in Cof'e. However, the data you send will not be submitted as you are below 18 year old")
                return redirect("common:thankyou_subject")

            with transaction.atomic():
                questionnaire_.subject = subject
                questionnaire_.save()

                subject.reset_cooldown()
                subject.save()

                audio_record = AudioRecord.objects\
                                          .filter(subject=subject)\
                                          .order_by("-upload_time")\
                                          .first()

                buffer, filename = audio_record.aws_file

                response = send_to_aws(buffer, filename)
                if response.status_code != 200:
                    messages.error(
                        request, "Please re-fill the questionnaire and try-again")
                    return render(request, "questionnaire/covid_contrib_quetionnaire.html", {'form': form, 'title': "Questionnaire"})

                return redirect('common:thankyou_subject')
        else:
            messages.error(
                request, "Please re-fill the questionnaire and try-again")
            return render(request, "questionnaire/covid_contrib_quetionnaire.html", {'form': form, 'title': "Questionnaire"})
    else:
        form = questionnaire()
        return render(request, "questionnaire/covid_contrib_quetionnaire.html", {'form': form, 'title': "Questionnaire"})

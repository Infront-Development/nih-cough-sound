from typing import Sized
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render
from django.utils.translation import gettext as _
from recording.models import Cough
from accounts.models import Subjects
# Create your views here.

def record(request):
    subject_id = request.session['subject_login']
    subject_details = Subjects.objects.get(subjects_login=subject_id)
    if request.is_ajax():
        audio = request.FILES.get('audio_data')
        print(audio," is here")
        print(type(audio), " type is hereeeeeee")
        record = Cough(cough_record=audio,subjects=subject_details)
        record.save()
    return render(request, 'record.html')

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

# Create your views here.
def consent(request):
    context = {
        'id': request.session['subject_login']
    }
    return render(request, 'consent-pop-up.html',context)

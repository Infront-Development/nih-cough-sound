from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from subjects.models import Cough

# Create your views here.

def record(request):
    if request.is_ajax():
        audio = request.FILES.get('audio_data')
        print(audio," is here")
        print(type(audio), " type is hereeeeeee")
        record = Cough(cough_record=audio)
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
from subjects.models import questionnairedata
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from subjects.forms import questionnaire
from subjects.models import Cough
import ssl
import cgi
import wave
import contextlib



# Create your views here.
def consent(request):
    return render(request, 'consent-pop-up.html')

def record(request):
    if request.is_ajax():
        audio = request.FILES.get('fd')
        print("data is here::;")
        print(audio)
        print(type(audio))
        record = Cough(cough_record=audio)
        record.save()
        print("audio is saved")
        # form = cgi.FieldStorage()
        # fname = form["fd"].filename
        # print("got filename : ", fname)
        # with contextlib.closing(wave.open(fname,'r')) as f:
        #     frames = f.getnframes()
        #     rate = f.getframerate()
        #     durations = frames / float(rate)
        #     print(durations)
    return render(request, 'record.html')

def viewRecording(request):
    record = Cough.objects.all()
    print("got data")
    context = {
        'record': record,
    }
    return render(request,'record.html',context)

def showForm(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        if form.is_valid():
            form.save()
            print("data successfully added!")
            #return redirect('viewVaccine')
        else:
            print("error: not working..")
    else:
        form = questionnaire()
    return render(request,"questionnaire.html",{'form':form})

def dataform(request):
    questdata = questionnairedata.objects().all()

def form_list_view(request):
    allforms = questionnairedata.objects.all()
    context = {'allforms': allforms}
    return render (request, 'formlist.html', context)
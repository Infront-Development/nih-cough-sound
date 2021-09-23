from subjects.models import questionnairedata
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from subjects.forms import questionnaire


# Create your views here.
def consent(request):
    return render(request, 'consent-pop-up.html')

def record(request):
    if request.is_ajax():
        audio = request.POST.get('fd')
        print(audio)
        form = questionnaire()
        return redirect('showForm')
    return render(request, 'record.html')

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
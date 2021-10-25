from django.contrib import messages
from django.shortcuts import redirect, render
from questionnaire.forms import questionnaire
from questionnaire.models import questionnairedata
from accounts.models import Subjects
# Create your views here.

#create questionnaire data
def questionnaire_form(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subjects.objects.get(subjects_login=request.session['subject_login'])
        if form.is_valid():
            form_details = form.save(commit=False)
            form_details.subject = subject
            form_details.save()
            return redirect('recording:cough_page')
    else:
        form = questionnaire()
    return render(request,"questionnaire/questionnaire.html",{'form':form, 'title' : "Questionnaire"})

#to view the questionnaire list
def view_questionnaire_list(request):
    allforms = questionnairedata.objects.all()
    context = {'allforms': allforms}
    return render (request, 'formlist.html', context)

def thank_subject(request):
    return render(request,'questionnaire/thanks_user.html')

from django.contrib import messages
from django.shortcuts import redirect, render
from questionnaire.forms import questionnaire
from questionnaire.models import questionnairedata
from accounts.models import Subjects
# Create your views here.

#create questionnaire data
def questionnaireForm(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subjects.objects.get(subjects_login=request.session['subject_login'])
        if form.is_valid():
            form_details = form.save(commit=False)
            form_details.subject = subject
            form_details.save()
            messages.success(request,'Welcome to NIH Cough Sound. ')
            return redirect('thank_subject')
    else:
        form = questionnaire()
    return render(request,"questionnaire.html",{'form':form})

#to view the questionnaire list
def viewQuestionnaireList(request):
    allforms = questionnairedata.objects.all()
    context = {'allforms': allforms}
    return render (request, 'formlist.html', context)

def thank_subject(request):
    return render(request,'thanks_user.html')

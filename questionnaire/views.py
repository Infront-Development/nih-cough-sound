from django.contrib import messages
from django.shortcuts import redirect, render
from questionnaire.forms import questionnaire
from questionnaire.models import QuestionnaireData
from accounts.models import Subject
from common.decorators import require_subject_login, must_agree_consent
# Create your views here.

#create questionnaire data
@require_subject_login
@must_agree_consent
def questionnaire_form(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subject.objects.get(phone_number=request.session['subject_login'])
        if form.is_valid():
            questionnaire_ = form.save(commit=False)
            if questionnaire_.age < 18: 
                messages.success(request, "Thank you for participating in NIH Cough Sound Project. However, the data you send will not be submitted as you are below 18 year old")
                return redirect("common:thankyou_subject")
            questionnaire_.subject = subject
            questionnaire_.save()
            return redirect('recording:record_main')
    else:
        form = questionnaire()
    return render(request,"questionnaire/questionnaire.html",{'form':form, 'title' : "Questionnaire"})

#to view the questionnaire list
@require_subject_login
@must_agree_consent
def view_questionnaire_list(request):
    allforms = QuestionnaireData.objects.all()
    context = {'allforms': allforms}
    return render (request, 'formlist.html', context)

def thank_subject(request):
    context ={
        'id': request.session['subject_login'],
        'title' : 'Cough Sound Project | Thank you for your participant',
        }
    return render(request,'questionnaire/thanks_user.html',context)

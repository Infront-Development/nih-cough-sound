from django.shortcuts import render, redirect
from .decorators import require_subject_login, must_agree_consent,cooldown
from common.forms import FeedbackForm
from accounts.models import Subject
from datetime import datetime, timedelta

@require_subject_login
@cooldown
def consent_page(request):
    if request.method == "GET":
        context = {
            'title': 'Cough Sound Project | Participant Agreement',
        }
        return render(request, "common/consent-pop-up.html", context)
    else:
        agree  = request.POST.get("agree")
        if int(agree) == 1:
            request.session['consent_agreed'] = 1 
            return redirect('recording:instruction_cough')
            # return redirect('questionnaire:questionnaire_form')



# @must_agree_consent
@require_subject_login
def feedback_subject(request):
  if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        subject = Subject.objects.get(phone_number=request.session['subject_login'])
        if feedback_form.is_valid():
            feedback_ = feedback_form.save()
            feedback_.subject = subject
            feedback_.save()
            subject.last_time = datetime.now()
            # subject.cooldown_exp = subject.last_time + timedelta(days=1)
            subject.save()
            return redirect('index')
  else:
        feedback_form = FeedbackForm()
  return render(request,"common/thank_you_feedback.html",{'feedback_form' :FeedbackForm(), 'title' : "Feedback"})


@require_subject_login
def thank_subject(request):
    # Clear consent agreed session if there is any  
    # if 'consent_agreed' in request.session:
    #     request.session.pop('consent_agreed')
    context ={
        'id': request.session['subject_login'],
        'title': "Thank you for contributing"
    }
    return render(request,"questionnaire/thanks_user.html",context)

#    if request.method == "POST":
#         context = {
#             'id' : request.session['subject_login'],
#             'feedback_form' :feedbackForm(),
#         }
#         return render(request, "questionnaire/feedback.html", context)


       
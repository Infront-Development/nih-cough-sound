from django.shortcuts import render, redirect
from functools import wraps
from django.contrib import messages
from .decorators import require_subject_login, must_agree_consent
from common.forms import feedbackForm
from accounts.models import Subjects

@require_subject_login
def consent_page(request):
    if request.method == "GET":
        context = {
            'id' : request.session['subject_login']
        }
        return render(request, "common/consent-pop-up.html", context)
    else:
        agree  = request.POST.get("agree")
        if (int(agree) == 1):
            request.session['consent_agreed'] = 1 
            return redirect('questionnaire:questionnaire_form')



@must_agree_consent
@require_subject_login
def feedback_subject(request):
  if request.method == 'POST':
        feedback_form = feedbackForm(request.POST)
        subject = Subjects.objects.get(phone_number=request.session['subject_login'])
        if feedback_form.is_valid():
            feedbackForm_ = feedback_form.save()
            feedbackForm_.subject = subject
            feedbackForm_.save()
            return redirect('common:thankyou_subject')
  else:
        feedback_form = feedbackForm()
  return render(request,"questionnaire/thank_you_feedback.html",{'feedback_form' :feedbackForm(), 'title' : "Feedback"})


@require_subject_login
def thank_subject(request):
    # Clear consent agreed session if there is any  
    if 'consent_agreed' in request.session:
        request.session.pop('consent_agreed')
    context ={'id': request.session['subject_login']}
    return render(request,"questionnaire/thanks_user.html",context)

#    if request.method == "POST":
#         context = {
#             'id' : request.session['subject_login'],
#             'feedback_form' :feedbackForm(),
#         }
#         return render(request, "questionnaire/feedback.html", context)


       
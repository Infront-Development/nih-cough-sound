from django.shortcuts import render, redirect
from functools import wraps
from django.contrib import messages
from .decorators import require_subject_login

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

@require_subject_login
def thank_subject(request):
    # Clear consent agreed session if there is any  
    if 'consent_agreed' in request.session:
        request.session.pop('consent_agreed')
    context ={'id': request.session['subject_login']}
    return render(request,'questionnaire/thanks_user.html',context)

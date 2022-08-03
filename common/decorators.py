from datetime import datetime
import numbers
from django.shortcuts import render, redirect
from functools import wraps
from accounts.models import Subject
from django.contrib import messages

def must_agree_consent(func):
    @wraps(func) 
    def wrap(request, *args, **kwargs):
        if 'consent_agreed' in request.session:
            return func(request, *args, **kwargs)
        else:
            messages.error(request, "You have to agree the consent first !") 
            return redirect('common:consent_page')
    return wrap
def require_subject_login(func):
    @wraps(func)
    def wrap(request,*args, **kwargs):
        if not 'subject_login' in request.session:
            messages.error(request, "You must register an account or login if you wish to proceed")

            return redirect('index')
        else:
            
            return func(request, *args, **kwargs)
    return wrap


def cooldown(func):
    @wraps(func)
    def wrap(request,*args, **kwargs):
        if not 'subject_login' in request.session:
            messages.error(request, "You must register an account or login if you wish to proceed")

            return redirect('index')
        else:
            # cooldown for 48 Hour after submission
            subject = Subject.objects.get(phone_number=request.session['subject_login'])
            if subject.cooldown_exp.isoformat() > datetime.today().isoformat():
                time_left = subject.cooldown_exp - datetime.today()
                days = time_left.days
                hours = int(time_left.seconds / 3600)
                
                if(days==1):
                 messages.error(request, "You must wait for "+ str(days) +" days "+str(hours) + " hours " +" before you can submit again")
                else:
                 messages.error(request, "You must wait for "+str(hours) + " hours " +" before you can submit again")
                return redirect('home')
            else :    
             return func(request, *args, **kwargs)
    return wrap
# Create your views here.


# def cooldown_timer(func):
#     @wraps(func)
#     def wrap(request,*args, **kwargs):
#         if 'subject_login' in request.session:

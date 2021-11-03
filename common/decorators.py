from django.shortcuts import render, redirect
from functools import wraps
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
# Create your views here.

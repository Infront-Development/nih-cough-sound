from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from subjects.models import questionnairedata


# Create your views here.
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            print("succesful login but failed to see page")
            return redirect('nav')
        else:
            print("not succesful login")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='loginView')
def staff_dashboard(request):
    return render(request,'staff_dashboard.html')

@login_required(login_url='loginView')
def nav(request):
    return redirect('staff_dashboard')

def logout(request):
    auth.logout(request)
    return redirect('loginView')

def identifier(request):
    return render(request,"id_form.html")
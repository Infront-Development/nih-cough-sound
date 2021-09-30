from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import registerSubjectsForm, loginSubjectsForm


# Create your views here.
def login(request):
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

@login_required(login_url='login')
def staff_dashboard(request):
    return render(request,'staff_dashboard.html')

@login_required(login_url='login')
def nav(request):
    return redirect('staff_dashboard')

def logout(request):
    auth.logout(request)
    return redirect('login')

def identifier(request):
    if request.method == 'POST':
        form1 = registerSubjectsForm(request.POST)
        form2 = loginSubjectsForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            print("subject is successfully created")
            return redirect('consent')
        elif form2.is_valid():
            return redirect('consent')
    else:
        form1 = registerSubjectsForm()
        form2 = loginSubjectsForm()
    return render(request,"id_form.html",{'form1':form1,'form2': form2})
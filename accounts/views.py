from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Subjects
from accounts.forms import registerSubjectsForm, loginSubjectsForm
import random
import string
from random import randrange
from accounts.models import Subjects

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
        form2 = loginSubjectsForm(request.POST)
        id_login = request.POST.get('subjects_login')
        if form1.is_valid():
            #commit false the form first
            subjectsDetails = form1.save(commit=False)
            #create identifier

            #Keep generating UNIQUE Identifier if a duplicate exists 
            while True:
                subject_login_id = create_unique_id(string.ascii_uppercase, subjectsDetails.subjects_phone_number)
                if not Subjects.objects.filter(subjects_login=subject_login_id).exists():
                    break

                
            subjectsDetails.subjects_login = subject_login_id
            request.session['subject_login'] = subjectsDetails.subjects_login
            subjectsDetails.save()

            messages.success(request,'Welcome to NIH Cough Sound, Please follow the instruction to ensure the best experience. Your ID is ' + subject_login_id + ' to login next time.')
            return redirect('recording:consent_page')
        elif id_login is not None:
            try:
                subjects_data = Subjects.objects.get(subjects_login=id_login)
                request.session['subject_login'] = subjects_data.subjects_login
                messages.success(request,'Welcome to NIH Cough Sound. ')
                return redirect('recording:consent_page')
            except Subjects.DoesNotExist:
                messages.error(request,'User is not found. Please check your user id. If you are a first timer, please click on the first time link.')
                return render(request,"id_form.html",{'form1':form1,'form2': form2})
    else:
        form1 = registerSubjectsForm()
        if 'subject_login' in request.session:
            login_id = request.session['subject_login']
            messages.info(request, "You have registered before please proceed with registered ID")
        else:
            login_id = ""
        
        form2 = loginSubjectsForm(initial={'subjects_login': login_id})
    return render(request,"id_form.html",{'form1':form1,'form2': form2})


def create_unique_id(choices, phonenumber):
    # Create 2 Random Alphabets
    alphabets = "".join([random.choice(string.ascii_letters) for i in range(2)])
    last_six_digits = phonenumber[-6:]
    return "{}{}".format(alphabets, last_six_digits)
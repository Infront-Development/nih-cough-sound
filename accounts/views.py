from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Subject
from accounts.forms import RegisterSubjectForm, LoginSubjectForm
import random
import string
from accounts.models import Subject
from django.utils.translation import gettext_lazy as _

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
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


def index(request):
    context = {}
    context['registration_form'] = RegisterSubjectForm()
    context['login_form'] = LoginSubjectForm(initial={
        'phone_number' : request.session['subject_login'] if 'subject_login' in request.session else "" 
        })
    return render(request, "id_form.html", context)

def register_participant(request):
    if request.method == "POST": 
        registration_form = RegisterSubjectForm(request.POST)
        if registration_form.is_valid():
             #commit false the form first
            new_subject = registration_form.save(commit=False)
            #create identifier
          
            #Keep generating UNIQUE Identifier if a duplicate exists 
            while True:
                subject_login_id = create_unique_id(string.ascii_uppercase, new_subject.phone_number)
                if not Subject.objects.filter(subject_login=subject_login_id).exists():
                    break

                
            new_subject.subject_login = subject_login_id
            request.session['subject_login'] = new_subject.phone_number
            new_subject.save()

            messages.success(request,str(_('Welcome to NIH Cough Sound, Please follow the instruction to ensure the best experience. Your ID is ')) + subject_login_id + str(_(' to login next time.')))
            return redirect('common:consent_page')
        else:
            messages.error(request, _("Please use a correct contact number format (01XXXXXXX). Up to 11 Digits"))
            
            return redirect("index")

def login_participant(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            subject = Subject.objects.get(phone_number=phone_number)

            # Set the subject login session 
            request.session['subject_login'] = subject.phone_number
            return redirect("common:consent_page")
        except Exception as e:
            messages.error(request, _("Phone number does not exist ! "))
            return redirect("index")
            


def create_unique_id(choices, phonenumber):
    # Create 2 Random Alphabets
    alphabets = "".join([random.choice(string.ascii_letters) for i in range(2)])
    last_six_digits = phonenumber[-6:]
    return "{}{}".format(alphabets, last_six_digits)

from django.shortcuts import redirect, render
from common.decorators import require_subject_login
from .models import DiagnoseResult
from accounts.models import Subject
from django.utils import timezone

# Create your views here.
@require_subject_login
def resultList(request):
    if DiagnoseResult.objects.filter(
        phone_number=request.session['subject_login']
    ):
        results = DiagnoseResult.objects.filter(
            phone_number=request.session['subject_login']
        )
    else:
        results = [
            {
                "covid_status": "High Risk",
                "confidence_rate": 69,
                "date_created": "2022-08-02 13:00:59.581915"
            },
            {
                "covid_status": "Low Risk",
                "confidence_rate": 70,
                "date_created": "2022-07-20 13:00:59.581915"
            },
            {
                "covid_status": "High Risk",
                "confidence_rate": 91,
                "date_created": "2022-07-13 13:00:59.581915"
            },
            {
                "covid_status": "Low Risk",
                "confidence_rate": 100,
                "date_created": "2022-02-09 13:00:59.581915"
            },
            {
                "covid_status": "Low Risk",
                "confidence_rate": 88,
                "date_created": "2022-01-01 13:00:59.581915"
            }
        ]
    context = {
        'id': request.session['subject_login'],
        "title": "Result",
        'results': results 
    }
    return render(request,"result-list.html",context)


@require_subject_login
def resultAnalysis(request):
    # TODO: POST and GET API
    response = {
        "covid_status": "Low Risk",
        "confidence_rate": 98,
        "phone_number": request.session['subject_login'],
        "subject": Subject.objects.get(phone_number=request.session['subject_login']),
        "date_created": timezone.now()
    }

    if True:
        result = DiagnoseResult.objects.create(**response)
    else:
        result = {
            "covid_status": "Low Risk",
            "confidence_rate": 98,
        }

    context = {
        "title": "Analyzed Result",
        'id': request.session['subject_login'],
        "result": result
    }
    return render(request,"result-analysis.html",context)
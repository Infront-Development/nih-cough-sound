from django.shortcuts import redirect, render
from common.decorators import require_subject_login
from .models import DiagnoseResult

# Create your views here.
@require_subject_login
def list_result(request):
    results = DiagnoseResult.objects.filter(
        phone_number=request.session['subject_login']
    ).order_by("-date_created")
    context = {
        'id': request.session['subject_login'],
        "title": "Result",
        'results': results 
    }
    return render(request,"result-list.html",context)

@require_subject_login
def analyse_result(request):
    result = DiagnoseResult.objects.filter(
            phone_number=request.session['subject_login']
        ).order_by("-date_created")[0]

    context = {
        "title": "Analyzed Result",
        'id': request.session['subject_login'],
        "result": result
    }
    return render(request,"result-analysis.html",context)
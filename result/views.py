from django.shortcuts import redirect, render
from common.decorators import require_subject_login
from .models import DiagnoseResult

from recording.models import AudioRecord

# Create your views here.


@require_subject_login
def list_result(request):
    results = DiagnoseResult.objects.filter(
        audio_record__in=AudioRecord.objects.filter(
            subject__phone_number=request.session['subject_login']
        )
    ).order_by("-date_created")
    context = {
        'id': request.session['subject_login'],
        "title": "Result",
        'results': results
    }
    return render(request, "result-list.html", context)


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
    return render(request, "result-analysis.html", context)


@require_subject_login
# can use phone number of 0199999999 for testing
def history_result(request):
    result_list = DiagnoseResult.objects.filter(
        audio_record__in=AudioRecord.objects.filter(
            subject__phone_number=request.session['subject_login']
        )
    ).order_by("-date_created")

    context = {
        'id': request.session['subject_login'],
        'title': "Result History",
        'result_list': result_list
    }
    return render(request, "history_result.html", context)


def edit_status(request):
    if request.method == 'POST':
        pk = request.POST.get('modal-title')
        result = DiagnoseResult.objects.get(id=pk)
        result.covid_status = request.POST.get('covid-status-value')
        result.save()
        return redirect('result/history_result')


def contribute_page(request):
    return render(request, "contribute_option.html")

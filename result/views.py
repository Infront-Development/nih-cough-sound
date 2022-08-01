from django.shortcuts import redirect, render
from common.decorators import require_subject_login
from .models import DiagnoseResult

# Create your views here.
@require_subject_login
def resultList(request):
    context = {
        'id': request.session['subject_login'],
        "title": "Result"
    }
    return render(request,"result-list.html",context)


@require_subject_login
def resultAnalysis(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        subject = Subject.objects.get(phone_number=request.session['subject_login'])
        if form.is_valid():
            questionnaire_ = form.save(commit=False)
            if questionnaire_.age < 18: 
                messages.success(request, "Thank you for participating in NIH Cough Sound Project. However, the data you send will not be submitted as you are below 18 year old")
                return redirect("common:thankyou_subject")
            questionnaire_.subject = subject
            questionnaire_.save()
            subject.save()
            return redirect('common:thankyou_subject')
    else:
        context = {
            "title": "Analyzed Result",
            'id': request.session['subject_login'],
        }
        return render(request,"result-analysis.html",context)
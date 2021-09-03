from django.shortcuts import render

# Create your views here.
def consent(request):
    return render(request, 'consent-pop-up.html')

def record(request):
    return render(request, 'record.html')
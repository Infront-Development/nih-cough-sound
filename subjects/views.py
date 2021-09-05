from django.shortcuts import render
from django.utils.translation import gettext as _
# Create your views here.
def consent(request):
    return render(request, 'consent-pop-up.html')

def record(request):
    if request.is_ajax():
        audio = request.POST.get('fd')
        print(audio)
    return render(request, 'record.html')
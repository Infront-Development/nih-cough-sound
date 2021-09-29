from django.shortcuts import render
# Create your views here.

#create questionnaire data
def questionnaireForm(request):
    if request.method == 'POST':
        form = questionnaire(request.POST)
        if form.is_valid():
            form.save()
            print("data successfully added!")
    else:
        form = questionnaire()
    return render(request,"questionnaire.html",{'form':form})

#to view the questionnaire list
def viewQuestionnaireList(request):
    allforms = questionnairedata.objects.all()
    context = {'allforms': allforms}
    return render (request, 'formlist.html', context)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.questionnaireForm, name="questionnaireForm"),
    path('viewQuestionnaireList/', views.viewQuestionnaireList, name="viewQuestionnaireList"),
]
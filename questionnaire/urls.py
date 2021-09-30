from django.urls import path
from . import views

urlpatterns = [
    path('questionnaireForm', views.questionnaireForm, name="questionnaireForm"),
    path('viewQuestionnaireList/', views.viewQuestionnaireList, name="viewQuestionnaireList"),
]
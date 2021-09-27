from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from subjects.models import questionnairedata
from . import views

urlpatterns = [
    path('record', views.record, name="record"),
    path('viewRecording', views.viewRecording, name="viewRecording"),
    path('viewBreathRecording', views.viewBreathRecording, name="viewBreathRecording"),   
]
from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views

urlpatterns = [
    path('cough', views.record, name="cough_page"),
    path('viewRecording', views.view_cough_recording, name="viewRecording"),
    path('viewBreathRecording', views.view_breath_recording, name="viewBreathRecording"),  
    path('breath',views.breath_page, name="breath_page")
     
]
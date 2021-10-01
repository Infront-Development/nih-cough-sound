from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views

urlpatterns = [
    path('record', views.record, name="record"),
    path('viewRecording', views.viewRecording, name="viewRecording"),
    path('viewBreathRecording', views.viewBreathRecording, name="viewBreathRecording"),  
    path('consent', views.consent, name="consent"),
    path('breathPage',views.breathPage, name="breathPage")
     
]
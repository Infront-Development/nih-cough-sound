from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views
app_name="recording"
urlpatterns = [
    path('cough', views.cough_page, name="cough_page"),
    # path('viewRecording', views.view_cough_recording, name="viewRecording"),
    path('breath',views.breath_page, name="breath_page"),
    path('instruc', views.instruc_page, name="instruc_page")
]

from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views

urlpatterns = [
    path('', views.consent, name="consent"),
]
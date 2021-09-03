from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.consent, name="consent"),
    path('record', views.record, name="record"),
]
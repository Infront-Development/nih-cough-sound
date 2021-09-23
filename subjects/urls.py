from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from subjects.models import questionnairedata
from . import views

urlpatterns = [
    path('', views.consent, name="consent"),
    path('record', views.record, name="record"),
    path('form', views.showForm, name="showForm"),
    path('formView', views.form_list_view, name='formView')
]
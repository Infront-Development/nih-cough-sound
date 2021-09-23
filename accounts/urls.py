from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from subjects.models import questionnairedata
from . import views

admin.site.site_header = "Cough Sound test"
admin.site.site_title = "Admin's Dashboard"


urlpatterns = [
    path('', views.loginView, name='loginView'),
    path("nav", views.nav, name="nav"),
    path('staff_dashboard',views.staff_dashboard, name='staff_dashboard'),
    path('logout',views.logout,name='logout'),
    path('formView', views.form_list_view, name='formView')
]
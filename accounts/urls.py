from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

admin.site.site_header = "Cough Sound test"
admin.site.site_title = "Admin's Dashboard"


urlpatterns = [
    path('login', views.loginView, name='loginView'),
    path("nav", views.nav, name="nav"),
    
]
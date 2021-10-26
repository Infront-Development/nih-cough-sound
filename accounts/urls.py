from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views

admin.site.site_header = "Cough Sound test"
admin.site.site_title = "Admin's Dashboard"


urlpatterns = [
    path('login', views.login, name='login'),
    path("nav", views.nav, name="nav"),
    path('staff_dashboard',views.staff_dashboard, name='staff_dashboard'),
    path('logout',views.logout,name='logout'),
    path('login-participant', views.login_participant, name="login_participant"),
    path('register-participant', views.register_participant, name="register_participant"),

    path('',views.index, name='index'),
] 

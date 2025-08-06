from django.contrib import admin
from django.urls import path

from . import views

admin.site.site_header = "Cough Sound test"
admin.site.site_title = "Admin's Dashboard"


urlpatterns = [
    path("login", views.login, name="login"),
    # path("nav", views.nav, name="nav"),
    # path('staff_dashboard',views.staff_dashboard, name='staff_dashboard'),
    # path('logout',views.logout,name='logout'),
    path("cough-test", views.cough_test, name="cough_test"),
    path(
        "tuberculosis-contribute",
        views.tuberculosis_contribute,
        name="tuberculosis_contribute",
    ),
    path("covid-contribute", views.covid_contribute, name="covid_contribute"),
    path("login-participant", views.login_participant, name="login_participant"),
    path(
        "register-participant", views.register_participant, name="register_participant"
    ),
    path("logout", views.logout, name="logout"),
    path("home", views.home, name="home"),
    path("", views.index, name="index"),
]

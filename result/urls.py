from django.urls import path
from . import views
app_name = "result"
urlpatterns = [
    path('', views.list_result, name="result_list"),
    path('analysis/', views.analyse_result, name="result_analysis"),
]
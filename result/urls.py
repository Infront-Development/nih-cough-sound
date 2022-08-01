from django.urls import path
from . import views
app_name = "result"
urlpatterns = [
    path('', views.resultList, name="result_list"),
    path('analysis/', views.resultAnalysis, name="result_analysis"),
]
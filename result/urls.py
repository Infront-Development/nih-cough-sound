from django.urls import path
from . import views
app_name = "result"
urlpatterns = [
    path('', views.list_result, name="result_list"),
    path('analysis/', views.analyse_result, name="result_analysis"),
    path('history_result', views.history_result, name="history_result"),
    path('update/status', views.edit_status, name="update_status"),
    path('contribute', views.contribute_page, name="contribute"),
]

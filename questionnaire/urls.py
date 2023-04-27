from django.urls import path
from . import views
app_name = "questionnaire"
urlpatterns = [
    path('questionnaire-form/', views.questionnaire_form,
         name="questionnaire_form"),
    path('tuberculosis-contribute-form', views.tuberculosis_questionnaire_form,
         name="tuberculosis-contribute-form"),
    path('view-questionnaire-list/', views.view_questionnaire_list,
         name="view_questionnaire_list"),
]

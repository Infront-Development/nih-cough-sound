from django.urls import path
from . import views

urlpatterns = [
    path('questionnaire-form/', views.questionnaire_form, name="questionnaire_form"),
    path('view-questionnaire-list/', views.view_questionnaire_list, name="view_questionnaire_list"),
    path('thank_you/', views.thank_subject, name="thank_subject"),
]
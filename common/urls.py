from . import views
from django.urls import path
app_name = 'common'

urlpatterns = [
    path('consent/', views.consent_page, name="consent_page"),
    path('feedback/', views.feedback_subject, name="feedback_subject"),
    path('thank-you/', views.thank_subject, name="thankyou_subject"),
    path('tuberculosis-contribution-aggreement', views.tuberculosis_contrib_aggreement_page,
         name="tuberculosis-contribution-aggreement"),
    path('covid-contribution-aggreement', views.covid_contrib_aggreement_page,
         name="covid-contribution-aggreement")
]

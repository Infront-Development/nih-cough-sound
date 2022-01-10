from django.urls import path 
app_name = 'common'

from . import views
urlpatterns = [
    path('consent/', views.consent_page, name="consent_page"),
    path('feedback/',views.feedback_subject,name="feedback_subject"),
    path('thank-you/', views.thank_subject, name="thankyou_subject"),
]
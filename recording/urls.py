from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views
app_name="recording"
urlpatterns = [
    path('cough', views.cough_page, name="cough_page"),
    path('cough-no-mask', views.cough_no_mask_page, name="cough_no_mask_page"),
    path('cough-with-mask', views.cough_with_mask_page, name="cough_with_mask_page"),
    # path('viewRecording', views.view_cough_recording, name="viewRecording"),
    path('breath',views.breath_page, name="breath_page"),
    path('breath-no-mask', views.breath_no_mask_page, name="breath_no_mask_page"),
    path('breath-with-mask', views.breath_with_mask_page, name="breath_with_mask_page"),
    path('instruc', views.instruc_page, name="instruc_page"),
    
    # Part Menu
    path('part-1-menu', views.part_1_menu_page, name="part_1_menu_page")

]

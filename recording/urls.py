from os import name
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic
from . import views
app_name="recording"
urlpatterns = [
    path('cough', views.cough_page, name="cough_page"),
    path('cough/part-1/', views.cough_no_mask_page, name="cough_no_mask_page"),
    path('cough/part-2/', views.cough_with_mask_page, name="cough_with_mask_page"),
    # path('viewRecording', views.view_cough_recording, name="viewRecording"),
    path('breath',views.breath_page, name="breath_page"),
    path('breath/part-1/', views.breath_no_mask_page, name="breath_no_mask_page"),
    path('breath/part-2/', views.breath_with_mask_page, name="breath_with_mask_page"),
    path('instruc', views.instruc_page, name="instruc_page"),
    path('instruc-cough', views.instruc_cough_page, name="instruc_cough_page"),
    path('instruc-breath', views.instruc_breath_page, name="instruc_breath_page"),


    # Part Menu
    path('part-1-menu', views.part_1_menu_page, name="part_1_menu_page"),
    path('part-2-menu', views.part_2_menu_page, name="part_2_menu_page")

]

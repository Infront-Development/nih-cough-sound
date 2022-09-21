from django.urls import path
from . import views
app_name="recording"
urlpatterns = [
    # path('main/', views.record_main, name="record_main"),

    path('cough/', views.instruction_cough, name="instruction_cough"),
    path('cough/record', views.record_cough, name="record_cough"),

    # path('cough/part-1/', views.cough_with_mask_page, name="cough_part_1"),
    # path('cough/part-2/', views.cough_no_mask_page, name="cough_part_2"),

    # path('breath/', views.instruc_breath_page, name="instruction_breath"),
    # path('breath/part-1/', views.breath_with_mask_page, name="breath_part_1"),
    # path('breath/part-2/', views.breath_no_mask_page, name="breath_part_2"),
    path('instruc', views.instruc_page, name="instruc_page"),
    
    ]

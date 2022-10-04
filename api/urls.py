from django.urls import path
app_name = "api"

from rest_framework.routers import DefaultRouter

from .views import APIintegrationViewset
router = DefaultRouter()
router.register(r'result', APIintegrationViewset, basename='result')

urlpatterns = [
]  +  router.urls
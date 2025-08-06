from django.urls import path

app_name = "api"

from rest_framework.routers import DefaultRouter

from .views import APIintegrationViewset, AuthenticatiorViewset

router = DefaultRouter()
router.register(r"result", APIintegrationViewset, basename="result")
router.register(r"token", AuthenticatiorViewset, basename="authentication")

urlpatterns = [] + router.urls

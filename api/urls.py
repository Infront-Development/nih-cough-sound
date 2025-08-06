from rest_framework.routers import DefaultRouter

from .views import APIintegrationViewset, AuthenticatiorViewset

app_name = "api"

router = DefaultRouter()
router.register(r"result", APIintegrationViewset, basename="result")
router.register(r"token", AuthenticatiorViewset, basename="authentication")

urlpatterns = [] + router.urls

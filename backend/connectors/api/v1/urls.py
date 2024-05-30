from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors135625ViewSet

router = DefaultRouter()
router.register(
    "testconnectors135625", Testconnectors135625ViewSet, basename="testconnectors135625"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]

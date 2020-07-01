from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import TestModelViewSet

router = DefaultRouter()
router.register("testmodel", TestModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import path, include
from rest_framework import routers

app_name = "board"

router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

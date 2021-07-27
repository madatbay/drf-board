from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"news", views.NewsViewSet)
router.register(r"comments", views.CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("news/upvote/<int:id>/", views.upvote_news, name='upvote'),
]
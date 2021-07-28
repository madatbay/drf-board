from django.http.response import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Comment, News
from .serializers import CommentSerializer, NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by("-created_at")
    serializer_class = NewsSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer


@api_view(["POST"])
def upvote_news(request, id):
    news = News.objects.get(id=id)
    news.upvotes += 1
    news.save()
    return HttpResponse(204)

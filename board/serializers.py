from rest_framework import serializers

from .models import Comment, News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ["title", "link", "upvotes", "author", "created_at"]
        read_only_fields = ["upvotes"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["news", "author_name", "content", "created_at"]

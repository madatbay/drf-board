from rest_framework import serializers

from .models import Comment, News


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "news", "author_name", "content", "created_at"]


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ["id", "title", "link", "upvotes", "author", "created_at", "comments"]
        read_only_fields = ["upvotes"]

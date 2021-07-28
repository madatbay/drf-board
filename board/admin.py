from django.contrib import admin
from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "author", "upvotes", "created_at")
    search_fields = ("title", "author", "created_at")
    list_filter = ("author", "created_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("news", "author_name", "content", "created_at")
    search_fields = ("author_name", "content")
    list_filter = ("author_name", "created_at")

from django.contrib import admin
from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ("title", "author", "created_at")
    list_filter = ("author", "created_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("author_name", "content")
    list_filter = ("author_name", "created_at")

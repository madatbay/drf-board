from django.db import models


class News(models.Model):
    title = models.CharField("Title", max_length=50)
    link = models.URLField("URL", max_length=200)
    upvotes = models.PositiveIntegerField("Upvotes")
    author = models.CharField("Author name", max_length=50)
    created_at = models.DateTimeField("Creation date", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField("Author", max_length=50)
    content = models.TextField("Comment")
    created_at = models.DateTimeField("Creation date", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.author_name

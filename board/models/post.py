from django.db import models
from django.contrib.auth.models import User

from .topic import Topic


class Post(models.Model):
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    topic = models.ForeignKey(
        Topic, related_name="posts", on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, null=True, related_name="+", on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    class Meta:
        db_table = "post"
        ordering = ("-created_at", )
        verbose_name = "post"
        verbose_name_plural = "posts"

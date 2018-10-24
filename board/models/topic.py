from django.db import models
from django.contrib.auth.models import User

from .board import Board


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(
        Board, related_name="topics", on_delete=models.CASCADE)
    starter = models.ForeignKey(
        User, related_name="topics", on_delete=models.CASCADE)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = "topic"
        ordering = ("subject", )
        verbose_name = "topic"
        verbose_name_plural = "topics"

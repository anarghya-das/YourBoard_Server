"""models"""
from django.db import models


class Board(models.Model):
    """Database model for each task"""
    user_id = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    isComplete = models.BooleanField(default=False)

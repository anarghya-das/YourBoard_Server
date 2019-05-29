"""models"""
from django.db import models


class Board(models.Model):
    """Board model"""
    user_id = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    isComplete = models.BooleanField(default=False)

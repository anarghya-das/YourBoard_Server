"""Serialize class"""
from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    """Serealizer"""
    class Meta:
        model = Board
        fields = '__all__'

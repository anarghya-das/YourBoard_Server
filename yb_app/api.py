"""This is the api class"""
from rest_framework import viewsets, permissions
from .models import Board
from .serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """View"""
    queryset = Board.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BoardSerializer
    filter_fields = ('user_id', 'title')

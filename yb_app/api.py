"""This is the api class"""
from rest_framework import viewsets, permissions
from .models import Board
from .serializers import BoardSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """View which sets the serializer class and adds flitering on user_id and title"""
    queryset = Board.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BoardSerializer
    filter_fields = ('user_id', 'title')

"""URLS module"""
from rest_framework import routers
from .api import BoardViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register('api/list', BoardViewSet, 'list')

urlpatterns = ROUTER.urls

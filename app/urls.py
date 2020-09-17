from django.urls import path, include
from rest_framework import routers
from app.viewsets import ProductosViewSet

router = routers.SimpleRouter()
router.register('productos',ProductosViewSet)

urlpatterns = []
urlpatterns += router.urls
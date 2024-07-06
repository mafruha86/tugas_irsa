from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router untuk otomatisasi routes
router = DefaultRouter()
router.register(r'kategori-batik', views.KategoriBatikViewSet)
router.register(r'item-batik', views.ItemBatikViewSet)
router.register(r'pelanggan', views.PelangganViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

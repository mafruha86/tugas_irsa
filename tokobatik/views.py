from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import KategoriBatik, ItemBatik, Pelanggan
from .serializers import KategoriBatikSerializer, ItemBatikSerializer, PelangganSerializer

# ViewSet untuk Kategori Batik
class KategoriBatikViewSet(viewsets.ModelViewSet):
    queryset = KategoriBatik.objects.all()
    serializer_class = KategoriBatikSerializer

# ViewSet untuk Item Batik
class ItemBatikViewSet(viewsets.ModelViewSet):
    queryset = ItemBatik.objects.all()
    serializer_class = ItemBatikSerializer

# ViewSet untuk Pelanggan
class PelangganViewSet(viewsets.ModelViewSet):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

from rest_framework import serializers
from .models import KategoriBatik, ItemBatik, Pelanggan

class KategoriBatikSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriBatik
        fields = ['id', 'nama']

class ItemBatikSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBatik
        fields = ['id', 'nama', 'kategori', 'harga', 'deskripsi']

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ['id', 'nama', 'email']

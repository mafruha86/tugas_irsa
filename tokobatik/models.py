from django.db import models

class KategoriBatik(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class ItemBatik(models.Model):
    nama = models.CharField(max_length=200)
    kategori = models.ForeignKey(KategoriBatik, related_name='items', on_delete=models.CASCADE)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama

class Pelanggan(models.Model):
    nama = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nama

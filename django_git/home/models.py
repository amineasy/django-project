from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Music(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='music_related')
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    octave = models.IntegerField()

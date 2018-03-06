from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(verbose_name="Bild", null=True, blank=True)
    name = models.CharField(verbose_name="Name", max_length=200, null=True, blank=True)
    title = models.CharField(verbose_name="Titel", max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name="Beschreibung", max_length=400, null=True, blank=True)
    ean = models.CharField(verbose_name="EAN", max_length=200, null=True, blank=True)
    size = models.CharField(verbose_name="Größe", max_length=200, null=True, blank=True)
    color = models.CharField(verbose_name="Farbe", max_length=200, null=True, blank=True)
    material = models.CharField(verbose_name="Stoff", max_length=200, null=True, blank=True)
    origin = models.CharField(verbose_name="Herkunft", max_length=200, null=True, blank=True)



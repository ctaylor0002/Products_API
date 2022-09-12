from pickletools import decimalnl_long
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image_link = models.CharField(max_length=500, blank=True) # Added in second migration
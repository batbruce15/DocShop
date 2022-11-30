from django.db import models

# Create your models here.
"""
Product (planification du modéle )
- nom
- prix
- quantité en stock
- description 
- image
"""


class Product(models.Model):
    nom = models.CharFeild(max_length=128)
    price = models.FloatFeild(default=0.0)
    stock = models.IntegerFeild(default=0)
    description = models.TextFeild(blank=True)
    thumbnail = models.ImageFeilf(Upload_to="products", blank=True, null=True)

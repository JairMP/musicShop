from typing import ChainMap
from django.db import models
from products.models import Product

class Category(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField(Product, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

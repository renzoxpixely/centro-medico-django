from django.db import models
from datetime import datetime
# Create your models here.







class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.PROTECT,
        default=1
    )
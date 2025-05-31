from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    class Meta:
        db_table = 'itw_product_category'
        verbose_name = 'product_category'
        verbose_name_plural = 'product_categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = 'itw_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField(max_length=50)
    default_price = models.FloatField(max_length=10, null=True, blank=True)
    description = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    product_category = models.ManyToManyField(ProductCategory, related_name='products')

    def __str__(self):
        return self.name


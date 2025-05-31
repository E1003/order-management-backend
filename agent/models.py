from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    class Meta:
        db_table = 'itw_customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    company_name = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

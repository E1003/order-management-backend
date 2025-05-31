import datetime

from django.contrib.auth.models import User

from agent.models import *
from product.models import *


# Create your models here.


class Order(models.Model):
    class Meta:
        db_table = 'itw_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    code = models.IntegerField()
    code_year = models.IntegerField()
    date_created = models.DateField(auto_now=True)
    date_registered = models.DateField()
    customer = models.ForeignKey('agent.Customer', on_delete=models.CASCADE, related_name='orders')
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderUnit(models.Model):
    class Meta:
        db_table = 'itw_order_unit'
        verbose_name = 'order_unit'
        verbose_name_plural = 'order_units'

    amount = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_units')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)


class Counter(models.Model):
    class Meta:
        db_table = 'itw_counter'
        verbose_name = 'counter'
        verbose_name_plural = 'counters'

    name = models.CharField(max_length=10, unique=True)
    value = models.IntegerField(default=0)

    @classmethod
    def get_or_create_for_current_year(cls):
        current_year = datetime.datetime.now().year
        counter, created = cls.objects.get_or_create(name=f'O-{current_year}', defaults={'value': 0})
        return counter

    @classmethod
    def get_or_create_customer_counter(cls):
        customer_counter, created = cls.objects.get_or_create(name='C', defaults={'value': 0})
        return customer_counter

    def increment(self):
        self.value += 1
        self.save()

    def reset(self):
        self.value = 0
        self.save()

from rest_framework import serializers

from .models import *


class OrderUnitSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = OrderUnit
        fields = ['product', 'product_name', 'amount', 'price']

    def get_product_name(self, obj):
        return f"{obj.product.name}"



class OrderWriteSerializer(serializers.ModelSerializer):
    order_units = OrderUnitSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_units', 'date_registered']

    def create(self, validated_data):
        order_units_data = validated_data.pop('order_units')
        order = Order.objects.create(**validated_data)
        for order_unit_data in order_units_data:
            OrderUnit.objects.create(order=order, **order_unit_data)
        return order

    def update(self, instance, validated_data):
        order_units_data = validated_data.pop('order_units')

        instance.order_units.all().delete()

        for order_unit_data in order_units_data:
            OrderUnit.objects.create(order=instance, **order_unit_data)

        instance = super(OrderWriteSerializer, self).update(instance, validated_data)

        return instance


class OrderReadSerializer(serializers.ModelSerializer):
    order_units = OrderUnitSerializer(many=True)
    customer_name = serializers.SerializerMethodField()
    date_registered = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ['code', 'code_year', 'id', 'customer', 'customer_name', 'date_registered', 'order_units']

    @staticmethod
    def get_date_registered(obj):
        return obj.date_registered

    def get_customer_name(self, obj):
        return f"{obj.customer.first_name} {obj.customer.last_name} {obj.customer.company_name}"
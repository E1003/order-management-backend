from rest_framework import serializers

from .models import *

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    product_category_names = serializers.SerializerMethodField()
    product_category = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'default_price', 'description', 'deleted', 'product_category', 'product_category_names']

    def get_product_category_names(self, obj):
        return [category.name for category in obj.product_category.all()]

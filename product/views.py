from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from agent.permissions import IsSeller
from rest_framework.permissions import IsAuthenticated

from .serializers import *
# Create your views here.

class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsSeller]


    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()

class ProductCategoryListAPIView(ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated, IsSeller]


class ProductCategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated, IsSeller]

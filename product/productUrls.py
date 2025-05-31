from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path('products/', ProductListAPIView.as_view(), name='products'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product'),
    path('categories/', ProductCategoryListAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', ProductCategoryRetrieveUpdateDestroyAPIView.as_view(), name='category'),
]


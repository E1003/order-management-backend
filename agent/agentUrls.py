from django.urls import path

from . import views
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,
    TokenRefreshView,)

urlpatterns = [
    path('user/', UserView.as_view(), name='user-detail'),
    path('customers/', CostumerListAPIView.as_view(), name='customers'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer'),
    path('sellers/', SellerListAPIView.as_view(), name='sellers'),
    path('sellers/<int:pk>/', SellerRetrieveUpdateDestroyAPIView.as_view(), name='seller'),
]


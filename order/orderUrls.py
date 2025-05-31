from django.urls import path

from . import views
from .views import *

urlpatterns = [

    path('orders/', OrderListAPIView.as_view(), name='orders'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order'),
]

from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from agent.permissions import IsSeller
from rest_framework.permissions import IsAuthenticated

from .serializers import *


# Create your views here.

class OrderListAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderWriteSerializer
    permission_classes = [IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        serializer.validated_data['creator'] = self.request.user

        counter = Counter.get_or_create_for_current_year()
        counter.increment()
        serializer.validated_data['code'] = counter.value
        serializer.validated_data['code_year'] = datetime.datetime.now().year

        serializer.save()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderWriteSerializer
        return OrderReadSerializer


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated, IsSeller]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return OrderWriteSerializer
        return OrderReadSerializer

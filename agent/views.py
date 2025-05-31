from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from order.models import Counter
from .permissions import IsAdministrator, IsSeller
from .serializers import *


# Create your views here.

class CostumerListAPIView(ListCreateAPIView):
    queryset = Customer.objects.filter(deleted=False)
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsSeller]

    def perform_create(self, serializer):
        serializer.save()

        counter = Counter.get_or_create_customer_counter()
        counter.increment()


class CustomerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.filter(deleted=False)
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsSeller]

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class SellerListAPIView(ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Seller', is_active=True)
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]

    def perform_create(self, serializer):
        user = serializer.save()
        seller_group = Group.objects.get(name='Seller')
        user.groups.add(seller_group)


class SellerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(groups__name='Seller')
    serializer_class = SellerSerializer
    permission_classes = [IsAuthenticated, IsAdministrator]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = Response(serializer.validated_data, status=200)

        access_token = serializer.validated_data.get('token', None)
        if access_token:
            response.set_cookie(
                key='access_token',
                value=access_token,
                httponly=True,
                secure=True,
                samesite='Lax'
            )
        return response


class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        return response


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
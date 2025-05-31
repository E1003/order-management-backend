from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        if self.instance is None:
            if User.objects.filter(email=value).exists():
                raise ValidationError('A user with that email already exists.')
        else:
            if User.objects.exclude(pk=self.instance.pk).filter(email=value).exists():
                raise ValidationError('A user with that email already exists.')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        seller_group = Group.objects.get(name='Seller')
        user.groups.add(seller_group)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'is_admin', 'token']

    def get_is_admin(self, obj):
        return obj.is_staff

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        super().validate(attrs)
        data = {}
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class UserDetailSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

    def get_role(self, obj):
        if obj.is_staff:
            return "Administrator"
        elif obj.groups.filter(name='Seller').exists():
            return "Seller"
        return "Unknown"
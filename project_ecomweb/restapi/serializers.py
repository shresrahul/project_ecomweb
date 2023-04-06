from rest_framework import serializers
from app_ecom.models import Product, Category
from django.contrib.auth.models import User

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'category_name',]
        model = Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'desc', 'category', 'price', 'quantity', 'cod', 'discount', 'user']
        model = Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        model = User

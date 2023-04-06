from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .serializers import CategorySerializers, ProductSerializer, UserSerializer
from app_ecom.models import Category, Product
from django.contrib.auth.models import User

# Create your views here.
class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        category_serializer = CategorySerializers(categories, many=True) # there will be many queries so -> many=true
        return Response(category_serializer.data, status=status.HTTP_200_OK)

class ProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        product_serialize = ProductSerializer(products, many=True)
        return Response(product_serialize.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        product_serialize = ProductSerializer(data=data)
        if product_serialize.is_valid():
            product_serialize.save()
            return Response({"msg": "Product added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(product_serialize.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductApiIdView(APIView):
    # This function will return object of product
    def get_object(self, id):
        try:
            product = Product.objects.get(id=id)
            return product
        except Product.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not Found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = ProductSerializer(instance=instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Something went wrong", "error": serializer.errors}, status=status.HTTP_404_NOT_ACCEPTABLE)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Data deleted successfully"}, status=status.HTTP_200_OK)

class UserApiView(APIView):
    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

class UserApiIdView(APIView):
    def get_object(self, id):
        try:
            user = User.objects.get(id=id)
            return user
        except User.DoesNotExist:
            return None
    
    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data not Found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = UserSerializer(instance=instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "Something went wrong", "error": serializer.errors}, status=status.HTTP_404_NOT_ACCEPTABLE)
        
    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Data Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Data deleted successfully"}, status=status.HTTP_200_OK)


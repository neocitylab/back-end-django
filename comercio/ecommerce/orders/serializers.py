from .models import Product, Category, Recipe, Subcategory
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (SerializerMethodField)
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User, Group

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class ProductSerializer(ModelSerializer):

    item_category= CategorySerializer(many=False)
    item_subcategory=SubcategorySerializer(many=False)
    class Meta:
        model = Product
        fields = '__all__'

class RecipeSerializer(ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class RegisterSerializer(RegisterSerializer):
    def create(self, request):
        user=super.create(request)
        group=Group.objects.get(name="Cliente")
        user.groups.add(group)
        user.save()
        return user
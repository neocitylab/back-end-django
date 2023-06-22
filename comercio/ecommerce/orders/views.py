from django.contrib.auth.models import Group, User
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.views.generic import ListView, CreateView, UpdateView, DeleteView 
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from django.shortcuts import render
from .models import Product, Category, Recipe
from .serializers import ProductSerializer, CategorySerializer, RecipeSerializer, UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class UserListView(ListView):
    model=User
    template_name='user_list.html'
    context_object_name='object_list'

class ProductView(ListView):
    model = Product
    template_name='product_list.html'
    context_object_name='object_list'

@permission_classes((AllowAny, ))
class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset=Product.objects.all().order_by('name')

@permission_classes((AllowAny, ))
class CategoryListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset=Category.objects.all().order_by('category_name')

@permission_classes((AllowAny, ))
class ProductCreateAPIView(CreateAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

@permission_classes((AllowAny, ))
class RecipeCreateAPIView(CreateAPIView):
    serializer_class=RecipeSerializer
    queryset=Recipe.objects.all()

@permission_classes((AllowAny, ))
class UserDetailAPIView(CreateAPIView):
    authentication_classes = (TokenAuthentication, )
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
@permission_classes((AllowAny, ))
class RegisterUserAPIView(CreateAPIView):
    serializer_class= RegisterSerializer
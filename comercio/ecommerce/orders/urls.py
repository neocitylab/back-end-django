from orders.views import UserListView, ProductView, ProductListApi, CategoryListApi, ProductCreateAPIView, RecipeCreateAPIView
from django.urls import path, re_path
from django.conf.urls.static import static


app_name = 'ordersAPI'

urlpatterns = [
    path('listView/', UserListView.as_view(), name='ListView'),
    path('productView/', ProductView.as_view(), name='productView'), 
    re_path(r"^getproducts$", ProductListApi.as_view(), name='getproducts'),
    re_path(r"^getcategories$", CategoryListApi.as_view(), name='getcategories'),
    re_path(r"^product$", ProductCreateAPIView.as_view(), name='product'), 
    re_path(r"^recipe$", RecipeCreateAPIView.as_view(), name='recipe')
]
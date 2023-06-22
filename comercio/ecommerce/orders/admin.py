from django.contrib import admin
from .models import Client, Product, Category, Recipe, Department, Country, City, Delivery, Subcategory

# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Department)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Delivery)
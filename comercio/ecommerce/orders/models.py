from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    id = models.IntegerField(null=False, primary_key=True, default=1)

    def full_name(self):
        return self.first_name +" "+self.last_name
    
    def __str__(self):
        return self.full_name()

class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, default="A")
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

class Subcategory(models.Model):

    subcategory_name = models.CharField(max_length=50, null=False, default="A")
    def __str__(self):
        return self.subcategory_name
    
    class Meta:
        verbose_name="Subcategory"
        verbose_name_plural="Subcategories"
        
class Product(models.Model):
    item_id=models.BigAutoField(primary_key=True)
    item_category= models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default=1)
    item_subcategory=models.ForeignKey(Subcategory, on_delete=models.PROTECT , null=False, default=1)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=200, null=False) 
    item_price = models.FloatField(verbose_name='$', null=False)    
    image_url=models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.name

 
class Country(models.Model):
    name=models.CharField(max_length=100, null=False, default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Country"
        verbose_name_plural="Countries"
       # db_table="Country"
    
class Department(models.Model):
    name=models.CharField(max_length=100, null=False)
    idCountry=models.ForeignKey(Country, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="Department"
        verbose_name_plural="Departments"

class City(models.Model):
    name=models.CharField(max_length=100, null=False)
    idDept=models.ForeignKey(Department, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return self.name      
    class Meta:
        verbose_name="City"
        verbose_name_plural="Cities"
    
class Delivery(models.Model):
    client_id=models.OneToOneField(Client,null=False, default=111, on_delete=models.CASCADE, blank=False)
    dv_city=models.ForeignKey(City, null=False, blank=False, on_delete=models.CASCADE)
    adress_main=models.CharField(max_length=100, null=False, blank=False, default="E")
    adress_complement=models.CharField(max_length=100, null=True, default="E")
    postal_code=models.IntegerField(null=False)

    def __str__(self):
        return str(self.client_id)
    
    class Meta:
        verbose_name="Delivery"
        verbose_name_plural="Deliveries"


class Recipe(models.Model):
    product_id=models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, default=100)
    client=models.ForeignKey(Client, on_delete=models.CASCADE, null=False, blank=False)
    address=models.ForeignKey(Delivery, on_delete=models.CASCADE)
    order_id=models.BigAutoField(primary_key=True)
    start_date=models.DateTimeField(null=False)
    end_date=models.DateTimeField(null=False)
    purchase_state=models.BooleanField(null=False)
    def __str__(self):
        return str(self.order_id)
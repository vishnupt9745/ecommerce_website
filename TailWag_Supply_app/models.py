from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_Seller=models.BooleanField(default=False)
    is_Customer=models.BooleanField(default=False)

class Customer(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE)
    customer_id=models.IntegerField(default=0)
    customer_name=models.CharField(max_length=20)
    customer_email=models.EmailField(max_length=254)
    customer_pnumber=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=100)
    customer_city=models.CharField(max_length=30)
    STATE_CHOICES = (
        ("kerala", "Kerala"),
        ("karnataka", "Karnataka"),
        ("tamil_nadu", "Tamil Nadu"),
        ("andhra_pradesh", "Andhra Pradesh"),
        ("telangana", "Telangana"),
        ("maharashtra", "Maharashtra"),
        ("gujarat", "Gujarat"),
        ("rajasthan", "Rajasthan"),
        ("uttar_pradesh", "Uttar Pradesh"),
        ("madhya_pradesh", "Madhya Pradesh"),
        ("bihar", "Bihar"),
        ("west_bengal", "West Bengal"),
        ("punjab", "Punjab"),
        ("odisha", "Odisha"),
    )

    customer_state=models.CharField(max_length=20,choices=STATE_CHOICES)


    def __str__(self):
        return self.customer_name


class Seller(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE)
    seller_id=models.IntegerField(default=0)
    seller_name=models.CharField(max_length=20)
    seller_email=models.EmailField(max_length=254)
    seller_pnumber=models.CharField(max_length=10)
    seller_address=models.CharField(max_length=100)

    def __str__(self):
        return self.seller_name


class Product_s(models.Model):
    product_user=models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=60)
    product_description = models.CharField(max_length=500, null=True, blank=True)
    product_brand = models.CharField(max_length=30, null=True, blank=True)
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TOYS', 'Toys'),
        ('COLLARS', 'Collars'),
        ('BEDS', 'Beds'),
        ('GROOMING', 'Grooming'),
        ('CLOTHING', 'Clothing'),
    ]
    product_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_img = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.product_name

class CartItem(models.Model):
    product = models.ForeignKey(Product_s, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'



class BuyNow(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_s, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    address = models.TextField()
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    order_date = models.DateTimeField(default=datetime.now)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"BuyNow: {self.customer.username} - {self.product.product_name}"





from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    phone_number = models.CharField(max_length=15, blank=True, unique=True)

#products model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name

#orders model
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=50 , default='Pending')
    date_placed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"Order {self.id} by {self.user.username}"

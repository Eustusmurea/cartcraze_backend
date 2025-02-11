from django.db import models
from .models import Product
from .models import user

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
   

    def __str__(self):
        return f"{self.user} - {self.product} ({self.quantity})"
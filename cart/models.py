from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    category= models.CharField(max_length=30)

    def __str__(self):
        return self.category
class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=1000,null=True)
    category= models.ForeignKey(Categories,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Cart(models.Model):
    name = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}({self.quantity})'
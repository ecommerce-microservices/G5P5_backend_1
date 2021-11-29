from django.db import models

class Product(models.Model):    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="product/img/")
    price = models.DecimalField(max_digits=60, decimal_places=2)

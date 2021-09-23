from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

class Product(models.Model):
    image = models.ImageField(upload_to="product-image", default='packageImage/blank.png', blank=True, null=True)
    name = models.CharField(max_length=40)
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    size = models.CharField(max_length=200, blank = True)
    description = models.TextField(blank = True)


from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)

    class Meta:        
        ordering = ('name',)        
        verbose_name = 'category'        
        verbose_name_plural = 'categories'    
    def __str__(self):        
        return self.name
    

class Product(models.Model):
    image = models.ImageField(upload_to="product-image", default='packageImage/blank.png', blank=True, null=True)
    name = models.CharField(max_length=40)
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category')
    size = models.CharField(max_length=200, blank = True)
    description = models.TextField(blank = True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:        
        ordering = ('name',)        
        index_together = (('id', 'slug'),)    

    def __str__(self):        
        return self.name
    
    def get_absolute_url(self):        
        return reverse('miswarfashionApp:product_detail',args=[self.id, self.slug])


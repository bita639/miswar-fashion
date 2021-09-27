from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Image

# Create your views here.

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    photo = Image.objects.all() 
    return render(request, 'gallery.html',{'photo': photo})


def product_detail(request, id, slug):    
    product = get_object_or_404(Product,id=id,slug=slug)    
    return render(request,'product_details.html',{'product': product})

def product_list(request):
    category = None    
    categories = Category.objects.all()    
    products = Product.objects.all()
    # products = Product.objects.filter(available=True)  
    # print(products)  
 
    return render(request,'index.html',{'categories': categories,'products': products})


def product_list_shop(request):
    category = None    
    categories = Category.objects.all()    
    products = Product.objects.all()
    # products = Product.objects.filter(available=True)  
    # print(products)  
 
    return render(request,'product.html',{'categories': categories,'products': products})
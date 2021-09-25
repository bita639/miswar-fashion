from django.urls import path
from . import views

app_name= 'miswarfashionApp'

urlpatterns = [
    path('', views.product_list, name='home'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products', views.product_list_shop, name='shop'),
    path('contact-us', views.contact, name='contact'),
    

]
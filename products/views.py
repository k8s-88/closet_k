from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})



def view_category(request, id):
    category = get_object_or_404(Category, pk=id)
    return render(request, "products/view_category.html", {"category": category})



def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_detail.html", {"product": product})
    
def home(request):
    return render(request, "products/home.html")
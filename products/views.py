from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def product_list(request):
    
    if "category" in request.GET:
        category = request.GET["category"]
        products = Product.objects.filter(category_id=category)
    else:
        products = Product.objects.all()
        
    
    return render(request, "products/product_list.html", {"products": products})


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_detail.html", {"product": product})
    
def home(request):
    return render(request, "products/home.html")
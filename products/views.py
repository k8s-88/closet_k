from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import SizeForm


# Create your views here.
def product_list(request):
    form = SizeForm()
    print('**************')
    print(form)
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products, "form": form})



def view_category(request, id):
    category = get_object_or_404(Category, pk=id)
    return render(request, "products/view_category.html", {"category": category})



def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "products/product_detail.html", {"product": product})
    
def home(request):
    return render(request, "products/home.html")
    
    

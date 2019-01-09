from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from products.models import Product
import json

# Create your views here.

def add_to_cart(request):
    product_id = request.POST['product']
    quantity = int(request.POST['quantity'])
    size = request.POST['size']

    products = Product.objects.all()
    cart = request.session.get('cart',{})

    
    if product_id in cart:
        if size in cart[product_id]:
            cart[product_id][size] += quantity
        else:
            cart[product_id].update({size:quantity})
    else:
        cart[product_id]={size:quantity}
        
    print(cart)    
   
    request.session['cart'] = cart
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render(request, "products/product_list.html", {"products": products})



def view_cart(request):
    cart = request.session.get('cart', {})
    
    
    cart_items = []
    cart_total =0
    
    for product_id, sizes in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        for size, quantity in sizes.items(): 
       
        
            cart_items.append({
                'id': product.id,
                'name': product.name,
                'brand': product.brand,
                'sku': product.sku,
                'size': size,
                'description': product.description,
                'image': product.image,
                'price': product.price,
                'stock': product.stock,
                'quantity': quantity,
                'total': product.price * quantity,
              
            })  
            
            cart_total += product.price * quantity
    
    return render(request, "cart/view_cart.html", {'cart_items': cart_items, 'cart_total': cart_total})
    
    
def remove_from_cart(request):
    product_id = request.POST['product']
    size = request.POST['size']
    cart = request.session.get('cart', {})
    del cart[product_id][size]
    request.session['cart'] = cart
    
    return redirect("/cart/view/")
    

    
    
    
    
    
    
    
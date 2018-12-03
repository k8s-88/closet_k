def items_in_cart(request):
    cart = request.session.get('cart', {})
    count = 0
    
    
    for product, sizes in cart.items():
        for quantity in sizes:
            
            count += sizes[quantity]
    return{'items_in_cart': count}
    
    

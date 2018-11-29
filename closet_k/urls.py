"""closet_k URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import signup, show_profile
from products.views import product_list, product_detail, home
from cart.views import add_to_cart, view_cart, remove_from_cart
from checkout.views import checkout, submit_payment
from django.views.static import serve
from django.conf import settings
from search.views import do_search





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('products/', product_list, name="products"),
    path('accounts/profile', show_profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('cart/add/', add_to_cart, name='add_to_cart'),
    path('cart/view/', view_cart, name='view_cart'),
    path('cart/remove/', remove_from_cart, name='remove_from_cart'),
    path('cart/checkout/', checkout, name='checkout'),
    path('checkout/pay/', submit_payment, name='submit_payment'),
    path('search/', do_search, name="search")


]
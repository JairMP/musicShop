from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from products.models import Product


def cart(request):

    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {})

def add(request):
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    cart.products.add(product)

    return render(request, 'carts/add.html', {
        'product': product
    })

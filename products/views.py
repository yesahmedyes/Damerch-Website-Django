from django.shortcuts import render
from .models import Product
from carts.views import cart


def product_list(request):
    cart_obj = cart(request)

    context = {
        'object_list': Product.objects.all(),
        'cart': cart_obj,
    }
    return render(request, "products/product_list.html", context=context)


def product_detail(request, slug):
    cart_obj = cart(request)

    context = {
        'object': Product.objects.get(slug=slug),
        'cart': cart_obj,
    }
    return render(request, "products/product_detail.html", context=context)


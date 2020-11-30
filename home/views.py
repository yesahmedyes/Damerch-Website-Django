from django.shortcuts import render
from .models import HomeImage, Gallery
from products.models import Product
from people.models import People
from subscribe.forms import SignupForm
from carts.views import cart


def home_page(request):
    try:
        request.session['cart_items']
    except KeyError:
        request.session['cart_items'] = 0

    cart_obj = cart(request)

    context = {
        'home_images': HomeImage.objects.filter(active=True),
        'gallery': Gallery.objects.filter(active=True),
        'products': Product.objects.filter(featured=True),
        'form': SignupForm,
        'people': People.objects.filter(featured=True),
        'cart': cart_obj
    }

    return render(request, "home.html", context)

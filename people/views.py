from django.shortcuts import render, reverse, redirect
from .models import People
from carts.views import cart
from django.contrib.auth.models import User


def people_list(request):
    cart_obj = cart(request)

    context = {
        'object_list': People.objects.all(),
        'cart': cart_obj,
    }
    return render(request, "people/people_list.html", context=context)


def people_detail(request, slug):
    cart_obj = cart(request)

    context = {
        'object': People.objects.get(slug=slug),
        'cart': cart_obj,
    }
    return render(request, "people/people_detail.html", context=context)


def artist_page(request, slug):
    if User.is_authenticated:
        cart_obj = cart(request)

        context = {
            'cart': cart_obj,
            'object': People.objects.get(slug=slug),
            'username': User.username,
        }
        return render(request, "people/artist.html", context=context)
    else:
        return redirect(reverse("myauth:artist"))


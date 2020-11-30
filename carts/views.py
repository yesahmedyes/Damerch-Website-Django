from django.shortcuts import render, redirect, reverse
from products.models import Product, Variation
from .models import Cart, CartItem
from django.http import HttpResponse
import json
from django.template.loader import render_to_string


def create(request):
    if request.user.is_authenticated:
        cart_obj = Cart.objects.create(user=request.user)
    else:
        cart_obj = Cart.objects.create(user=None)
    return cart_obj


def cart(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        cart_obj = create(request)
        request.session['cart_id'] = cart_obj.id
    else:
        try:
            cart_obj = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart_obj = create(request)
            request.session['cart_id'] = cart_obj.id
        if request.user.is_authenticated and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    return cart_obj


def cart_home(request):
    cart_obj = cart(request)
    request.session['cart_items'] = cart_obj.cartitem_set.count()
    context = {
        'cart': cart_obj,
    }
    return render(request, "carts/view.html", context=context)


def cart_update(request):
    cart_obj = cart(request)
    slug = request.POST.get('product', None)
    tag = request.POST.get('size', None)
    qty = request.POST.get('qty', None)

    if slug is not None:
        try:
            product = Product.objects.get(slug=slug)
            try:
                variation = product.variation_set.get(tag=tag)
            except Variation.DoesNotExist:
                variation = None
        except Product.DoesNotExist:
            return redirect(reverse('home:home'))

        cart_item = None
        cart_item_exits = None

        for item in cart_obj.cartitem_set.all():
            if item.product.id == product.id:
                if variation is not None:
                    if item.variation.tag == variation.tag:
                        cart_item = item
                        cart_item_exits = True
                else:
                    cart_item = item
                    cart_item_exits = True
                    break

        if cart_item_exits is not True:
            cart_item = CartItem()
            cart_item.product = product
            if variation is not None:
                cart_item.variation = variation
            cart_item.cart = cart_obj

        new_qty = cart_item.quantity + int(qty)
        cart_item.quantity = new_qty

        if cart_item.quantity <= 0:
            cart_item.delete()
        else:
            cart_item.save()

        cart_obj = cart_calculate(request)

        if request.is_ajax():
            data = {
                'line_total': str(new_qty * cart_item.product.price),
                'cart_total': str(cart_obj.total),
                'product_qty': str(new_qty),
                'price': str(cart_item.product.price),
                'var': str(cart_item.variation.title),
                'total_qty': str(cart_obj.cartitem_set.count()),
            }
            if cart_item_exits is not True:
                context = {
                    'item': cart_item,
                }
                template = render_to_string('base/modal.html', context=context, request=request)
                data.update({'new_template': template})
            return HttpResponse(json.dumps(data), content_type="application/json")

    return redirect(reverse('carts:cart'))


def cart_calculate(request):
    cart_obj = cart(request)
    cart_obj.total = 0
    for item in cart_obj.cartitem_set.all():
        item.line_total = item.quantity * item.product.price
        cart_obj.total += item.line_total
        item.save()
    cart_obj.save()
    return cart_obj


def cart_delete(request):
    cart_obj = cart(request)
    slug = request.POST.get('product', None)
    tag = request.POST.get('size', None)

    if slug is not None:
        product = Product.objects.get(slug=slug)
        try:
            variation = product.variation_set.get(tag=tag)
        except Variation.DoesNotExist:
            variation = None

        cart_item = None

        for item in cart_obj.cartitem_set.all():
            if item.product.id == product.id:
                if variation is not None:
                    if item.variation.tag == variation.tag:
                        cart_item = item
                        break
                else:
                    cart_item = item
                    break

        cart_item.delete()
        cart_obj = cart_calculate(request)

    cart_obj.cartitem_set.count()

    if request.is_ajax():
        data = {
            'cart_total': str(cart_obj.total),
            'item_count': str(cart_obj.cartitem_set.count()),
        }
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return redirect(reverse('carts:cart'))

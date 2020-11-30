from django.shortcuts import render, reverse, redirect
from carts.views import cart
from .models import Order
from carts.models import Cart
from django.core.mail import send_mail
from django.template.loader import render_to_string


def checkout(request):
    cart_obj = cart(request)

    context = {
        'cart': cart_obj,
    }

    if cart_obj.cartitem_set.all().count() < 1:
        return redirect(reverse("home:home"))

    object_id = request.session.get("object_id", None)

    if object_id is not None:
        new_object = Order.objects.get(pk=object_id or None)
        if new_object.fname is not None:
            context.update({'fname': new_object.fname})
        if new_object.lname is not None:
            context.update({'lname': new_object.lname})
        if new_object.address is not None:
            context.update({'address': new_object.address})
        if new_object.city is not None:
            context.update({'city': new_object.city})
        if new_object.country is not None:
            context.update({'country': new_object.country})
        if new_object.email is not None:
            context.update({'email': new_object.email})
        if new_object.phone is not None:
            context.update({'phone': new_object.phone})

    else:
        if request.user.is_authenticated:
            user = request.user
            if user.email:
                context.update({'email': user.email.title()})
            if user.first_name:
                context.update({'fname': user.first_name})
            if user.last_name:
                context.update({'lname': user.last_name})

    return render(request, "checkout/checkout.html", context=context)


def payment(request):
    fname = request.POST.get('fname' or None)
    lname = request.POST.get('lname' or None)
    address = request.POST.get('address' or None)
    city = request.POST.get('city' or None)
    country = request.POST.get('country' or None)
    email = request.POST.get('email' or None)
    phone = request.POST.get('phone' or None)

    object_id = request.session.get("object_id", None)
    cart_id = request.session.get("cart_id", None)

    if object_id is None:
        new_object = Order.objects.create(
            cart=Cart.objects.get(pk=cart_id),
            fname=fname, lname=lname, address=address,
            city=city, country=country, email=email, phone=phone
        )
        new_object.save()
        request.session['object_id'] = new_object.id
    else:
        new_object = Order.objects.get(pk=object_id)
        if fname is not None:
            new_object.fname = fname
        if lname is not None:
            new_object.lname = lname
        if address is not None:
            new_object.address = address
        if city is not None:
            new_object.city = city
        if country is not None:
            new_object.country = country
        if email is not None:
            new_object.email = email
        if phone is not None:
            new_object.phone = phone
        new_object.save()

    return render(request, "checkout/payment.html")


def order(request):
    object_id = request.session.get("object_id", None)
    pm = request.POST.get("payment-method", None)

    if object_id is not None and pm is not None:
        new_object = Order.objects.get(pk=object_id)
        new_object.payment_method = pm
        new_object.order_status = 'received'
        if pm == 'card':
            new_object.transaction_done = True
        new_object.save()

        # context = {
        #     'name': new_object.fname,
        #     'order_number': object_id,
        #     'link': request.build_absolute_uri(reverse("checkout:order_status", args=(new_object.id,))),
        #     'cart': new_object.cart,
        # }

        # text_temp = render_to_string('checkout/order_email.txt', context=context)
        # html_temp = render_to_string('checkout/order_email.html', context=context)
        #
        # send_mail(
        #     subject='Your order status',
        #     message=text_temp,
        #     from_email='damerch <no-reply@damerch.co>',
        #     recipient_list=['{email}'.format(email=new_object.email)],
        #     html_message=html_temp,
        #     fail_silently=False,
        # )

        del request.session["object_id"]
        del request.session["cart_id"]

        for item in new_object.cart.cartitem_set.all():
            item.product.sold += item.quantity
            item.product.save()

        return redirect(reverse("checkout:order_success", args=(new_object.id, )))
    else:
        return redirect(reverse("checkout:checkout"))


def order_success(request, id):
    email = Order.objects.get(pk=id).email
    context = {
        "status": Order.objects.get(pk=id).order_status,
        "id": id,
        'message': "A confirmation email is being sent to {email}. Make sure you check the spam folder if it's not in your inbox.".format(email=email),
    }
    return render(request, "checkout/order.html", context=context)


def order_status(request, id):
    context = {
        "status": Order.objects.get(pk=id).order_status,
        "id": id,
    }
    return render(request, "checkout/order.html", context=context)

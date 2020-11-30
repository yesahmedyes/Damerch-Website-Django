from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from carts.views import cart
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from people.models import People


@csrf_protect
def login_page(request):
    username = request.POST.get("username" or None)
    password = request.POST.get("password" or None)

    cart_obj = cart(request)

    context = {
        'cart': cart_obj,
    }

    if username is not None:
        if password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home:home"))
            else:
                context.update({'message': 'The login credentials were invalid.'})

    return render(request, "auth/login.html", context=context)


@csrf_protect
def artist_login(request):
    username = request.POST.get("username" or None)
    password = request.POST.get("password" or None)

    cart_obj = cart(request)

    context = {
        'cart': cart_obj,
    }

    user = None
    slug = None
    if username is not None:
        if password is not None:
            for p in People.objects.all():
                if p.user.username == username:
                    user = authenticate(request, username=username, password=password)
                    slug = p.slug
                    break
            if user is not None:
                login(request, user, backend='django.contrib.myauth.backends.ModelBackend')
                return redirect(reverse("people:admin", args=(slug,)))
            else:
                context.update({'message': 'The login credentials were invalid.'})

    return render(request, "auth/artist_login.html", context=context)


def login_landing(request, redirected):
    cart_obj = cart(request)

    context = {
        'cart': cart_obj,
    }

    if redirected == 'register':
        context.update({'message': 'A confirmation email has been sent to you.'})

    return render(request, "auth/login.html", context=context)


def logout_page(request):
    logout(request)
    return redirect(reverse("myauth:login"))


def reset_main(request):
    email = request.POST.get("email" or None)

    cart_obj = cart(request)

    context = {
        'cart': cart_obj,
    }

    if email is not None:
        user = User.objects.filter(email=email).first()
        if user is not None:
            data = {
                'name': user.username,
                'link': request.build_absolute_uri(reverse("myauth:reset_page", args=(email,))),
            }
            text_temp = render_to_string('auth/reset_email.txt', context=data)
            html_temp = render_to_string('auth/reset_email.html', context=data)
            send_mail(
                subject='Reset your password',
                message=text_temp,
                from_email='damerch <no-reply@damerch.co>',
                recipient_list=['{email}'.format(email=email)],
                html_message=html_temp,
                fail_silently=False,
            )
            context.update({'message': 'A reset email has been sent to you.'})
        else:
            context.update({'message': 'No user exists with that email.'})

    return render(request, "auth/reset_landing.html", context=context)


def reset_page(request, id):
    new_password = request.POST.get("password" or None)

    if new_password is not None:
        user = User.objects.get(email=id)
        user.set_password(new_password)
        user.save()
        return redirect(reverse("myauth:login"))

    cart_obj = cart(request)

    context = {
        'email': id,
        'cart': cart_obj,
    }

    return render(request, "auth/reset.html", context=context)


def register_page(request):
    username = request.POST.get("username" or None)
    email = request.POST.get("email" or None)
    password = request.POST.get("password" or None)
    repassword = request.POST.get("repassword" or None)

    cart_obj = cart(request)

    context = {
        'cart': cart_obj,
    }

    if (username is not None) and (email is not None):
        if (password is not None) and (password == repassword):
            if User.objects.filter(username=username).exists():
                context.update({
                    'message': 'Sorry, Username already exists.'
                })
            else:
                if User.objects.filter(email=email).exists():
                    context.update({
                        'message': 'Sorry, Email already exists.'
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.is_active = False
                    user.save()

                    context = {
                        'name': username,
                        'link': request.build_absolute_uri(reverse("myauth:register_success", args=(email,))),
                    }
                    text_temp = render_to_string('auth/register_email.txt', context=context)
                    html_temp = render_to_string('auth/register_email.html', context=context)
                    send_mail(
                        subject='Welcome! Confirm your email',
                        message=text_temp,
                        from_email='damerch <no-reply@damerch.co>',
                        recipient_list=['{email}'.format(email=email)],
                        html_message=html_temp,
                        fail_silently=False,
                    )
                    redirected = "register"
                    return redirect(reverse("myauth:login_landing", args=(redirected,)))
    return render(request, "auth/register.html", context=context)


def register_success(request, id):
    user = User.objects.get(email=id)
    user.is_active = True
    user.save()
    login(request, user, backend='django.contrib.myauth.backends.ModelBackend')
    return redirect(reverse("home:home"))

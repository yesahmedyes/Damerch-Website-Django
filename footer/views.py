from django.shortcuts import render
from django.core.mail import send_mail


def refund_page(request):
    return render(request, "footer/refund.html")


def faq_page(request):
    return render(request, "footer/faq.html")


def contact_page(request):
    name = request.POST.get("name" or None)
    email = request.POST.get("email" or None)
    query = request.POST.get("query" or None)
    details = request.POST.get("details" or None)

    context = {

    }

    if email is not None:
        send_mail(
            subject='Contact - {s}'.format(s=query),
            message='{d}, \n\nfrom name: {n} with {e} '.format(d=details, n=name, e=email),
            from_email='damerch <no-reply@damerch.co>',
            recipient_list=['damerch.o@gmail.com'],
            fail_silently=False,
        )
        context.update({'message': 'Your query has been received. We will get back to you at the earliest.'})

    return render(request, "footer/contact.html", context=context)


def about_page(request):
    return render(request, "footer/about.html")


def ps_page(request):
    return render(request, "footer/ps.html")


def tos_page(request):
    return render(request, "footer/tos.html")


def career_page(request):
    return render(request, "footer/career.html")

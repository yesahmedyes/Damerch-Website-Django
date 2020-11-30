from django.db.models import Q
from products.models import Product
from subscribe.forms import SignupForm
from django.shortcuts import render


def product_list(request):
    products = Product.objects.none()
    q = request.GET.get('q')
    s = request.GET.get('s', 'All')
    c = request.GET.get('c', 'All')

    if q is not None:
        lookups = (Q(title__icontains=q)
                   | Q(keywords__icontains=q)
                   | Q(owner__name__icontains=q)
                   | Q(description__icontains=q)
                   )
        temp = Product.objects.filter(lookups).distinct()
    else:
        temp = Product.objects.all()

    if s != 'All':
        for product in temp:
            exists = False
            for item in product.variation_set.all():
                if item.tag == s:
                    exists = True
            if exists:
                products |= Product.objects.filter(pk=product.pk)
    else:
        products = temp

    context = {
        'object_list': products,
        'form': SignupForm,
        'q': q,
        's': s,
        'c': c
    }
    return render(request, "products/product_list.html", context=context)

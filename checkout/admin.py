from django.contrib import admin
from django.shortcuts import resolve_url, reverse
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.utils.html import format_html
from .models import Order
from carts.models import Cart


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('cart_link', 'fname', 'lname', 'address', 'city', 'country', 'email', 'phone', 'payment_method', 'transaction_done', 'order_status',)
    list_display = ('pk', 'email', 'order_status', 'payment_method', 'transaction_done')
    list_filter = ('order_status', 'payment_method', 'transaction_done')
    readonly_fields = ('cart_link',)

    def cart_link(self, obj):
        url = resolve_url(admin_urlname(Cart._meta, 'change'), obj.cart.id)
        return format_html('<a href="{url}">Cart - {name}</a>'.format(url=url, name=str(obj.cart)))


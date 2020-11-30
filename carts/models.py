from django.db import models
from django.contrib.auth.models import User
from products.models import Product, Variation


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    total = models.DecimalField(default=0.0, max_digits=20, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.cart.id) + ": " + self.product.title


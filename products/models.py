from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from merch.utils import unique_slug
from people.models import People


class Product(models.Model):
    owner = models.ForeignKey(People, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    delivery = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=00.00)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    featured = models.BooleanField(default=False)
    sold = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def get_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


def product_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug(instance)


pre_save.connect(product_pre_save, sender=Product)


VAR_CATEGORIES = [
    ('size', 'size')
]


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title + ": " + str(self.id)


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=120)
    tag = models.CharField(max_length=10)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.title + ": " + self.title

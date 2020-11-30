from django.db import models
from carts.models import Cart


PM_CATEGORIES = [
    ('cod', 'cash on delivery'),
    ('card', 'credit or debit card'),
]

STATUS_CATEGORIES = [
    ('received', 'received'),
    ('processed', 'processed'),
    ('delivered', 'delivered'),
]


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False, blank=False, related_name='order')
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    payment_method = models.CharField(max_length=120, choices=PM_CATEGORIES)
    transaction_done = models.BooleanField(default=False)
    order_status = models.CharField(max_length=120, choices=STATUS_CATEGORIES, null=True, blank=True)

    def __str__(self):
        return str(self.id)

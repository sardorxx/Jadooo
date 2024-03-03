from django.db import models
from uuid import uuid4

from account.models import CustomUser
from shop.models import Product


class Orders(models.Model):
    # red
    OPTION1 = 'Paring'
    # orange
    OPTION2 = 'Sending'
    # yellow
    OPTION3 = 'Ready'
    # green
    OPTION4 = 'Delivered'

    CHOICES = [
        (OPTION1, 'Paring'),
        (OPTION2, 'Sending'),
        (OPTION3, 'Ready'),
    ]

    PAY_STATUS = "Before"
    PAY_STATUS1 = "After"
    PAY_CHOICE = [
        (PAY_STATUS, "Before"),
        (PAY_STATUS1, "After"),
    ]

    order_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_amount = models.DecimalField(max_digits=9, decimal_places=2)
    is_delivery = models.BooleanField(default=False)
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=7, choices=CHOICES, default=OPTION1)
    payment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)


class UserCards(models.Model):
    card_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_number = models.IntegerField()
    expiration_date = models.DateField()
    security_code = models.IntegerField()
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

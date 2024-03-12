from django.db import models
from uuid import uuid4
from account.models import CustomUser


# Create your models here.

class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class SubCategory(models.Model):
    subcategory_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)


class Product(models.Model):
    OPTION1 = 'Child'
    OPTION2 = 'Men'
    OPTION3 = 'Women'
    OPTION4 = 'Animal'
    OPTION5 = 'Everybody'
    OPTION6 = 'Girls'
    OPTION7 = 'Boby'
    OPTION8 = 'Home'
    OPTION9 = 'Office'

    CHOICES = [
        (OPTION1, 'Child'),
        (OPTION2, 'Men'),
        (OPTION3, 'Women'),
        (OPTION4, 'Animal'),
        (OPTION5, 'Everybody'),
        (OPTION6, 'Girls'),
        (OPTION7, 'Boby'),
        (OPTION8, 'Home'),
        (OPTION9, 'Office'),
    ]
    product_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(max_length=255)
    for_who = models.CharField(
        max_length=20,
        choices=CHOICES,
        default=OPTION5,
    )
    image = models.ImageField(upload_to='image/product/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=20)
    amount_of_products = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.CharField(max_length=20)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    is_deleted = models.BooleanField(default=False)


class Images(models.Model):
    image_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    name_products = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/Products/')
    created_at = models.DateTimeField(auto_now_add=True)


class ImageEdit(models.Model):
    imageedit_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    image_name = models.CharField(max_length=100)
    is_edit = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Basket(models.Model):
    basket_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)


class Messages(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user')
    message_text = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    is_read = models.BooleanField(default=False)



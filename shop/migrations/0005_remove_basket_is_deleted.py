# Generated by Django 5.0.2 on 2024-03-08 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_basket_quantity_basket_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='is_deleted',
        ),
    ]

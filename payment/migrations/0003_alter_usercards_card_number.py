# Generated by Django 5.0.2 on 2024-03-02 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_usercards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercards',
            name='card_number',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.0.5 on 2023-08-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_remove_delivery_the_orders_he_ro_she_has_won_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='تایید شده'),
        ),
    ]

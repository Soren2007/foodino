# Generated by Django 4.0.5 on 2023-08-04 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_remove_delivery_the_orders_he_ro_she_has_won'),
        ('orders', '0005_remove_orderdetails_register_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery', verbose_name='پیک'),
        ),
    ]

# Generated by Django 4.0.5 on 2023-08-04 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_is_delivery_alter_customer_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city', verbose_name='شهر'),
        ),
    ]

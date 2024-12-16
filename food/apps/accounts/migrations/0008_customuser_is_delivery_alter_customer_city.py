# Generated by Django 4.0.5 on 2023-08-03 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customer_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_delivery',
            field=models.BooleanField(default=False, help_text='در صورتی  که این تیک را فعال کنید کاربر به عنوان پیک شناخته می شود و می تواند به آدرس سفارشات دسترسی پیدا کند.', verbose_name='پیک است بله/خیر'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city', verbose_name='شهر'),
        ),
    ]

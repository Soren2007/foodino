# Generated by Django 4.0.5 on 2023-08-01 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customer_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='current_order',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد سفارش جاری'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='delivered_order',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد سفارش تحویل داده شده'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='returned_order',
            field=models.PositiveIntegerField(default=0, verbose_name='تعداد سفارش مرجوع شده'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city', verbose_name='شهر'),
        ),
    ]

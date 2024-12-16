# Generated by Django 4.0.5 on 2023-08-04 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_customuser_city_customuser_state_alter_customer_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, help_text='آدرسی که می خواهید سفارش به آنجا ارسال شود', null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(help_text='شهری که سفارش به آن ارسال می شود.', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city', verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, help_text='شما تماسی است که وضعیت سفارش به آن ارسال می\u200cشود', max_length=11, null=True, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.ForeignKey(help_text='استانی  که سفارش به آن ارسال شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.state', verbose_name='استان یا ایالت'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]

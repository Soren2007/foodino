# Generated by Django 4.0.5 on 2023-08-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_delivery_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='your_last_activity',
            field=models.DateTimeField(auto_now=True, verbose_name='آخرین فعالیت شما'),
        ),
    ]

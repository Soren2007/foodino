# Generated by Django 4.0.5 on 2023-08-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0005_alter_ad_ad_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='ad_is_active',
            field=models.BooleanField(default=False, help_text='', verbose_name='فعال/غیرفعال'),
        ),
    ]

# Generated by Django 4.0.5 on 2023-08-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0015_alter_ad_ad_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='ad_is_active',
            field=models.BooleanField(default=False, help_text='', verbose_name='فعال/غیرفعال'),
        ),
    ]

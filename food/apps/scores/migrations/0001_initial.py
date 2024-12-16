# Generated by Django 4.0.5 on 2023-07-30 01:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Scoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ درج')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(5)], verbose_name='امتیاز')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoring_food', to='food.food', verbose_name='غذا')),
                ('scoring_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoring_user', to=settings.AUTH_USER_MODEL, verbose_name='امتیاز دهنده')),
            ],
            options={
                'verbose_name': 'امتیاز',
                'verbose_name_plural': 'امتیازات',
            },
        ),
    ]

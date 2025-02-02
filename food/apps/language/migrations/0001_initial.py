# Generated by Django 4.0.5 on 2023-07-30 01:07

import apps.language.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(max_length=20, verbose_name='کد زبان')),
                ('language_name', models.CharField(max_length=120, verbose_name='نام زبان به انگلیسی')),
                ('language_directionality', models.CharField(default='rtl', max_length=120, verbose_name='راست چین یا چپ چین زبان')),
                ('language_is_active', models.BooleanField(default=False, verbose_name='قعال/غیرفعال')),
            ],
            options={
                'verbose_name': 'زبان',
                'verbose_name_plural': 'زبان\u200cها',
                'db_table': 'table_languages',
            },
        ),
        migrations.CreateModel(
            name='LanguageFont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('font_name', models.CharField(max_length=100, verbose_name='نام فونت')),
                ('font_embedded_opentype_format', models.FileField(blank=True, help_text='s', null=True, upload_to='C:\\Users\\asus\\Desktop\\Programming\\nojavankharazmi\\food/static/fonts', validators=[apps.language.models.validate_language_font_font_file_embedded_opentype], verbose_name='افایل فونت .eot')),
                ('font_truetype_format', models.FileField(blank=True, help_text='s', null=True, upload_to='C:\\Users\\asus\\Desktop\\Programming\\nojavankharazmi\\food/static/fonts', validators=[apps.language.models.validate_language_font_font_file_truetype], verbose_name='افایل فونت .ttf')),
                ('font_woff_format', models.FileField(blank=True, help_text='s', null=True, upload_to='C:\\Users\\asus\\Desktop\\Programming\\nojavankharazmi\\food/static/fonts', validators=[apps.language.models.validate_language_font_font_file_woff], verbose_name='افایل فونت .woff')),
                ('font_woff_2_format', models.FileField(blank=True, help_text='s', null=True, upload_to='C:\\Users\\asus\\Desktop\\Programming\\nojavankharazmi\\food/static/fonts', validators=[apps.language.models.validate_language_font_font_file_woff_2], verbose_name='افایل فونت .woff')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.language', verbose_name='زبان')),
            ],
            options={
                'verbose_name': 'فونت',
                'verbose_name_plural': 'فونت\u200cها',
                'db_table': 'table_languages_fonts',
            },
        ),
    ]

# Generated by Django 4.0.5 on 2023-07-30 01:07

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='عنوان هدیه')),
                ('description', models.TextField(verbose_name='توضیحات هدیه')),
                ('background_color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='رنگ پس زمینه')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='رنگ متن')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
            ],
            options={
                'verbose_name': 'هدیه',
                'verbose_name_plural': 'هدایا',
                'db_table': 'table_gift',
            },
        ),
        migrations.CreateModel(
            name='wheel_of_luck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='عنوان گردونه شانس')),
                ('description', models.TextField(verbose_name='توضیحات گردونه شانس')),
                ('max_user_score', models.PositiveIntegerField(default=30, verbose_name='حداقل امتیاز کاربر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
                ('gifts', models.ManyToManyField(to='gift.gift', verbose_name='هدایا گردونه شانس')),
            ],
            options={
                'verbose_name': 'گردونه شانس',
                'verbose_name_plural': 'گردونه\u200cهای شانس',
                'db_table': 'table_gift_wheel_of_luck',
            },
        ),
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان قرعه کشی')),
                ('image', models.ImageField(help_text='لطفا غکس خود را بارگذاری کنید. نکته: بهتر است فرمت فایل بارگذاری شده webp باشد تا در سرعت سایت مشکلی پیش نیاید.', upload_to='images/gift/lottery/Lottery', verbose_name='بنر قرغه کشی')),
                ('description', models.TextField(verbose_name='توضیحات قرعه کشی')),
                ('start_of_the_lottery', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ و زمان شروع قرعه کشی')),
                ('is_done', models.BooleanField(default=False, verbose_name='انجام شده؟')),
                ('is_start', models.BooleanField(default=False, verbose_name='مجوز شروع را دارد؟')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('user_number', models.PositiveIntegerField(default=1, verbose_name='تعداد کاربر')),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
                ('gifts', models.ManyToManyField(help_text='کاربرانی که انتخاب میشوند این جایزه را هدیه می گیرند', to='gift.gift', verbose_name='جایزه برنده')),
            ],
            options={
                'verbose_name': 'قرعه کشی',
                'verbose_name_plural': 'قرعه کشی\u200cها',
                'db_table': 'table_gift_lottery',
            },
        ),
    ]

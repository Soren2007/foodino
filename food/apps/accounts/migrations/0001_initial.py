# Generated by Django 4.0.5 on 2023-07-30 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gift', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='نام کشوری که در آن خدمات صورت می گیرد را وارد کنید.', max_length=250, verbose_name='نام کشور')),
                ('photo_of_the_flag', models.ImageField(blank=True, default='images/account/country/NaN.png', help_text='تصویر پرچم کشوری که در آن خدمات صورت می گیرد را وارد کنید. نکته : بهتر است از تصویر با فرمت webp استفاده کنید تا سرعت سایت به مشکل بر نخورد', null=True, upload_to='images/account/country', verbose_name='عکس پرجم کشور')),
                ('telephone_code', models.CharField(blank=True, default='+98', help_text='در این قسمت باید کد پیش شماره کشور را وارد کنید تا در زمان ارسال پیامک کدپیش شماره ابتدای شماره تماس کاربر بیفتد.', max_length=50, null=True)),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
            ],
            options={
                'verbose_name': 'کشور',
                'verbose_name_plural': 'کشورها',
                'db_table': 'table_country',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='استانی که در آن خدمات صورت می\u200cگیرد آن را وارد کنید.', max_length=50, verbose_name='نام استان')),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
                ('country', models.ForeignKey(blank=True, help_text='استان در کدام کشور است؟ آن را وارد کنید.', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country', verbose_name='کشور')),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان\u200cها',
                'db_table': 'table_state',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='شهری که در آن خدمات صورت می\u200cگیرد را وارد کنید.', max_length=200, verbose_name='نام شهر')),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
                ('country', models.ForeignKey(blank=True, help_text='شهر در کدام کشور قرار دارد آن را وارد کنید.', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country', verbose_name='کشور')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهرها',
                'db_table': 'table_city',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('mobile_number', models.CharField(blank=True, help_text='شماره موبایل کاربر جدید را وارد کنید. نکته: شماره تماس کاربر نمی\u200cتواند تکراری باشد.', max_length=11, null=True, unique=True, verbose_name='شماره موبایل')),
                ('username', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='نام کاربری')),
                ('name', models.CharField(blank=True, help_text='نام کاربر را وارد کنید. نکته: این فیلد اجباری نیست.', max_length=50, verbose_name='نام')),
                ('family', models.CharField(blank=True, help_text='نام خانوادگی کاربر را وارد کنید. نکته: این فیلد اجباری نیست.', max_length=50, verbose_name='نام خانوادگی')),
                ('profile', models.ImageField(blank=True, default='images/account/profile/NaN.png', help_text='تصویر کاربر را بارگذاری کنید. نکته:بهتراست از تصاویری به فرمت webp استفاده کنید تا سرعت سایت به مشکل برنخورد. نکته: این فیلد اجباری نیست.', null=True, upload_to='images/account/profile', verbose_name='پروفایل')),
                ('email', models.EmailField(blank=True, help_text='ایمیل کاربر را وارد کنید. در صورتی که کاربر ایمیل خود را وارد کرده باشد ایمیل\u200cهایی از طرف سایت برای او ارسال می\u200cشود', max_length=200, verbose_name='ایمیل')),
                ('gender', models.CharField(blank=True, choices=[('True', 'مرد'), ('False', 'زن')], default='True', help_text='نکته: این فیلد اجباری نیست.', max_length=50, null=True, verbose_name='جنسیت')),
                ('address', models.TextField(help_text='لطفا آدرس محل زنگی کاربر را به درستی وارد کنید. نکته: این فیلد در زمان ثبت\u200cنام اجباری نیست.', max_length=500, verbose_name='آدرس')),
                ('birth_date', models.DateField(blank=True, help_text='تاریخ تولد کار بر را وارد کنید. با وارد کردن تاریخ تولد کاربر روز تولد آن پیام تبریک برای آن ارسال می\u200cشود.', null=True, verbose_name='تاریخ تولد')),
                ('score', models.IntegerField(default=20, help_text='امتیاز کاربر امتیازی است که با هر خرید به آن اضافه می شود. و با آن می\u200cتواند گردونه شانس را فعال کند.', verbose_name='امتیاز')),
                ('national_code', models.CharField(blank=True, help_text='لظفا کدملی کاربر را درست وارد کنید زیرا که اگر مشکلی به وجود بی آید با آن کارهای قانونی انجام شود.', max_length=11, null=True, verbose_name='کدملی')),
                ('postal_code', models.CharField(blank=True, help_text='لطفا کدپستی کاربر را وارد کنید تا سایت بتواند خدمات بهتری به کاربر بدهد', max_length=10, null=True, verbose_name='کدپستی')),
                ('register_date', models.DateField(default=django.utils.timezone.now, help_text='تاریخ ثبت\u200cنام کاربر به ضورت خودکار نوشته می\u200cشود.', verbose_name='تاریخ ثبت نام')),
                ('is_complete_information', models.BooleanField(default=False, help_text='در صورتی که کاربر تمامی اطلاعات را داده باشد این تیک فعال می شود.', verbose_name='اطلاعات کامل است؟')),
                ('is_active', models.BooleanField(default=False, help_text='با این فیلد شما می\u200cتوانید کابر را فعال و یا غیر فعال کنید.', verbose_name='وضعیت فعال/غیرفعال')),
                ('active_code', models.CharField(blank=True, help_text='کدفعال سازی کدی است که به صورت خودکار ساخته می شود و برای راستی آزمایی کاربر به او پیانک می\u200cشود و کاربر می تواند با وارد کردن آن کاربر فعال شود.', max_length=100, null=True, verbose_name='کد فعال سازی')),
                ('is_admin', models.BooleanField(default=False, help_text='در صورتی که این تیک فعال شود کاربر مدیر سایت شناخته می شود و به برخی از قسمت\u200cهای خصوصی دسترسی پیدا میکند. توجه: درصورتی که کاربر خلاف کار باشد باعث به خطر افتادن اطلاعات سایت می\u200cشود در تایین وضعیت این فیلد بسیار دقت کنیدو', verbose_name='مدیر است بله/خیر')),
                ('is_support', models.BooleanField(default=False, help_text='درصورتی که این تیک را فعال کنید کاربر به عنوان پشتیبان شناخته می شود و دسترسی به پنل پیام ها دسترسی پیدا می کند.', verbose_name='پشتیبان است بله/خیر')),
                ('is_serviceman', models.BooleanField(default=False, help_text='در صورتی  که این تیک را فعال کنید کاربر به عنوان خدماجی شناخته می شود و می تواند وضعبت سفارش کاربر را کنترل کند.', verbose_name='خدماتچی است بله/خیر')),
                ('is_translated_content', models.BooleanField(default=False, verbose_name='آیا محتوا ترجمه شده؟')),
                ('country', models.ForeignKey(blank=True, help_text='کشوری که کاربر در آن زندگی می کند.', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country', verbose_name='کشور')),
                ('gifts', models.ManyToManyField(blank=True, help_text='هدایایی است که کاربر طی فعالیت ها دریافت می کند.', to='gift.gift', verbose_name='هدایای کاربر')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر سفارشی',
                'verbose_name_plural': 'کاربران سفارشی',
                'db_table': 'table_custom_user',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(blank=True, help_text='شما تماسی است که وضعیت سفارش به آن ارسال می\u200cشود', max_length=11, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='images/account/profile/NaN.png', null=True, upload_to='images/account/profile')),
                ('city', models.ForeignKey(help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.city', verbose_name='شهر')),
                ('country', models.ForeignKey(help_text='کشوری که سفارش به آن ارسال شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.country', verbose_name='کشور')),
                ('state', models.ForeignKey(help_text='شهری شهری که سفارش به آن ارسال شود', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.state', verbose_name='استان یا ایالت')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتریان',
                'db_table': 'table_customer',
            },
        ),
    ]

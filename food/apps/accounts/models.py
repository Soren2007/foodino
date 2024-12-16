from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,PermissionsMixin,BaseUserManager,UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.gift.models import Gift
__version__ = "1.1.0"
# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self,mobile_number,email="",name="",family="",active_code=None,gender=None,password=None):
        if not mobile_number:
            raise ValueError(_("شماره موبایل باید وارد شود"))
        if len(mobile_number)<11:
            raise ValueError(_('شماره موبایل وارد شده صحیح نمی باشد.'))
        user = self.model(
            mobile_number=mobile_number,
            email=self.normalize_email(email),
            name=name,
            family=family,
            active_code=active_code,
            gender=gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,mobile_number,email,name,family,password=None,active_code=None,gender=None):
        user=self.create_user(
            mobile_number=mobile_number,
            email=email,
            name=name,
            family=family,
            active_code=active_code,
            gender=gender,
            password=password,
        )
        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
# start class Country
class Country(models.Model):
    class_name="Country"
    name = models.CharField(max_length=250,verbose_name=_("نام کشور"),help_text=_("نام کشوری که در آن خدمات صورت می گیرد را وارد کنید."))
    photo_of_the_flag = models.ImageField(upload_to='images/account/country',verbose_name=_("عکس پرجم کشور") ,default="images/account/country/NaN.png", null=True,blank=True,help_text=_("تصویر پرچم کشوری که در آن خدمات صورت می گیرد را وارد کنید. نکته : بهتر است از تصویر با فرمت webp استفاده کنید تا سرعت سایت به مشکل بر نخورد"))
    telephone_code = models.CharField(max_length=50,default="+98",help_text=_("در این قسمت باید کد پیش شماره کشور را وارد کنید تا در زمان ارسال پیامک کدپیش شماره ابتدای شماره تماس کاربر بیفتد."),null=True,blank=True)
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"photo_of_the_flag","verbose_name":"تصویر پرچم کشور","value":self.photo_of_the_flag},{'field_name':'name',"verbose_name":"نام کشور","value":self.name},{'field_name':'telephone_code',"verbose_name":"کدپیش شماره کشور","value":self.telephone_code}]
    # def __dict__(self):
    #     return {"name":self.name,"photo_of_the_flag":self.photo_of_the_flag,"telephone_code":self.telephone_code}
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = _("کشور")
        verbose_name_plural = _("کشورها")
        db_table ="table_country"

# end class Country   
# start class State   
class State(models.Model):
    class_name = "State"
    name = models.CharField(max_length=50,verbose_name=_("نام استان"),help_text=_("استانی که در آن خدمات صورت می‌گیرد آن را وارد کنید."))
    country = models.ForeignKey(Country,verbose_name=_("کشور"),on_delete=models.CASCADE,null=True,blank=True,help_text=_("استان در کدام کشور است؟ آن را وارد کنید."))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"name","verbose_name":"نام استان یا ایالت","value":self.name},{"field_name":"country","verbose_name":"کشور","value":self.country}]
    def __str__(self):
        return f"{self.name} {self.country}"
    class Meta:
        verbose_name = _("استان")
        verbose_name_plural = _("استان‌ها")
        db_table ="table_state"
# end class State   
# start class City   
class City(models.Model):
    class_name = "City"
    name = models.CharField(max_length=200,verbose_name=_("نام شهر"),help_text=_("شهری که در آن خدمات صورت می‌گیرد را وارد کنید."))
    country = models.ForeignKey(Country,verbose_name=_("کشور"),on_delete=models.CASCADE,null=True,blank=True,help_text=_("شهر در کدام کشور قرار دارد آن را وارد کنید."))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"country","verbose_name":'کشور',"value":self.country},{"field_name":"name","verbose_name":"نام شهر","value":self.name}]
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = _("شهر")
        verbose_name_plural = _("شهرها")
        db_table ="table_city"
# end class City   
# start class CustomUser   
class CustomUser(AbstractBaseUser,PermissionsMixin):
    class_name = "CustomUser" 
    mobile_number = models.CharField(max_length=11,verbose_name=_("شماره موبایل"),unique=True,null=True,blank=True,help_text=_("شماره موبایل کاربر جدید را وارد کنید. نکته: شماره تماس کاربر نمی‌تواند تکراری باشد."))
    username = models.CharField(max_length=20,verbose_name=_("نام کاربری"),unique=True,null=True,blank=True)
    name = models.CharField(max_length=50,blank=True, verbose_name=_("نام"),help_text=_("نام کاربر را وارد کنید. نکته: این فیلد اجباری نیست."))
    family = models.CharField(max_length=50,blank=True, verbose_name=_("نام خانوادگی"),help_text=_("نام خانوادگی کاربر را وارد کنید. نکته: این فیلد اجباری نیست."))
    profile = models.ImageField(upload_to='images/account/profile',verbose_name=_("پروفایل") ,default="images/account/profile/NaN.png", null=True,blank=True,help_text=_("تصویر کاربر را بارگذاری کنید. نکته:بهتراست از تصاویری به فرمت webp استفاده کنید تا سرعت سایت به مشکل برنخورد. نکته: این فیلد اجباری نیست."))
    email = models.EmailField(max_length=200,blank=True,verbose_name=_("ایمیل"),help_text=_("ایمیل کاربر را وارد کنید. در صورتی که کاربر ایمیل خود را وارد کرده باشد ایمیل‌هایی از طرف سایت برای او ارسال می‌شود"))
    GENDER_CHOICES=(('True',_('مرد')),('False',_('زن')))
    gender= models.CharField(max_length=50,blank=True,choices=GENDER_CHOICES,default='True',null=True, verbose_name="جنسیت",help_text=_("نکته: این فیلد اجباری نیست."))
    address = models.TextField(max_length=500,verbose_name=_("آدرس"),help_text=_("لطفا آدرس محل زنگی کاربر را به درستی وارد کنید. نکته: این فیلد در زمان ثبت‌نام اجباری نیست."))
    latitude_location = models.CharField(max_length=15,blank=True,null=True,verbose_name=_("عرض جغرافیایی کاربر"))
    longitude_location = models.CharField(max_length=15,blank=True,null=True,verbose_name=_("طول جغرافیایی کاربر"))
    country = models.ForeignKey(Country,verbose_name=_("کشور"),on_delete=models.CASCADE,null=True,blank=True,help_text=_("کشوری که کاربر در آن زندگی می کند."))
    state = models.ForeignKey(State,verbose_name=_("استان"),on_delete=models.CASCADE,null=True,blank=True,help_text=_("استانی که کاربر در آن زندگی می کند."))
    city = models.ForeignKey(City,verbose_name=_("شهر"),on_delete=models.CASCADE,null=True,blank=True,help_text=_("شهری که کاربر در آن زندگی می کند."))
    birth_date = models.DateField(null=True,verbose_name=_("تاریخ تولد"),blank=True,help_text=_("تاریخ تولد کار بر را وارد کنید. با وارد کردن تاریخ تولد کاربر روز تولد آن پیام تبریک برای آن ارسال می‌شود."))
    score = models.IntegerField(default=20,verbose_name=_("امتیاز"),help_text=_("امتیاز کاربر امتیازی است که با هر خرید به آن اضافه می شود. و با آن می‌تواند گردونه شانس را فعال کند."))
    national_code = models.CharField(null=True,verbose_name=_("کدملی"),blank=True, max_length=11,help_text=_("لظفا کدملی کاربر را درست وارد کنید زیرا که اگر مشکلی به وجود بی آید با آن کارهای قانونی انجام شود."))
    postal_code = models.CharField(null=True,verbose_name=_("کدپستی"),blank=True, max_length=10,help_text=_("لطفا کدپستی کاربر را وارد کنید تا سایت بتواند خدمات بهتری به کاربر بدهد"))
    register_date= models.DateField(default=timezone.now, verbose_name=_("تاریخ ثبت نام"),help_text=_("تاریخ ثبت‌نام کاربر به ضورت خودکار نوشته می‌شود."))
    is_complete_information = models.BooleanField(default=False,verbose_name=_("اطلاعات کامل است؟"),help_text=_("در صورتی که کاربر تمامی اطلاعات را داده باشد این تیک فعال می شود."))
    is_active = models.BooleanField(default=False, verbose_name="وضعیت فعال/غیرفعال",help_text=_("با این فیلد شما می‌توانید کابر را فعال و یا غیر فعال کنید."))
    active_code= models.CharField(max_length=100,null=True, blank=True, verbose_name=_("کد فعال سازی"),help_text=_("کدفعال سازی کدی است که به صورت خودکار ساخته می شود و برای راستی آزمایی کاربر به او پیانک می‌شود و کاربر می تواند با وارد کردن آن کاربر فعال شود."))
    gifts = models.ManyToManyField(Gift,verbose_name=_("هدایای کاربر"),help_text=_("هدایایی است که کاربر طی فعالیت ها دریافت می کند."),blank=True)
    current_order = models.PositiveIntegerField(default=0,verbose_name=_("تعداد سفارش جاری"))
    delivered_order = models.PositiveIntegerField(default=0,verbose_name=_("تعداد سفارش تحویل داده شده"))
    returned_order = models.PositiveIntegerField(default=0,verbose_name=_("تعداد سفارش مرجوع شده"))
    is_admin = models.BooleanField(default=False, verbose_name=_("مدیر است بله/خیر"),help_text=_("در صورتی که این تیک فعال شود کاربر مدیر سایت شناخته می شود و به برخی از قسمت‌های خصوصی دسترسی پیدا میکند. توجه: درصورتی که کاربر خلاف کار باشد باعث به خطر افتادن اطلاعات سایت می‌شود در تایین وضعیت این فیلد بسیار دقت کنیدو"))
    is_support = models.BooleanField(default=False, verbose_name=_("پشتیبان است بله/خیر"),help_text=_("درصورتی که این تیک را فعال کنید کاربر به عنوان پشتیبان شناخته می شود و دسترسی به پنل پیام ها دسترسی پیدا می کند."))
    is_serviceman = models.BooleanField(default=False, verbose_name=_("خدماتچی است بله/خیر"),help_text=_("در صورتی  که این تیک را فعال کنید کاربر به عنوان خدماجی شناخته می شود و می تواند وضعبت سفارش کاربر را کنترل کند."))
    is_delivery = models.BooleanField(default=False, verbose_name=_("پیک است بله/خیر"),help_text=_("در صورتی  که این تیک را فعال کنید کاربر به عنوان پیک شناخته می شود و می تواند به آدرس سفارشات دسترسی پیدا کند."))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS=['email','name','family']
    objects  = CustomUserManager()
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"mobile_number","verbose_name":"شماره موبایل","value":self.mobile_number},{"field_name":"name","verbose_name":"نام","value":self.name},{"field_name":"family","verbose_name":"نام خانوادگی","value":self.family},{"field_name":"profile","value":self.profile,"verbose_name":"پروفایل"},{"field_name":"email","verbose_name":"ایمیل","value":self.email},{"field_name":"gender","verbose_name":"جنسیت","value":self.gender},{"field_name":"address","verbose_name":"آدرس","value":self.address},{"field_name":"country","verbose_name":"کشور","value":self.country},{"field_name":"birth_date","verbose_name":"تاریخ تولد","value":self.birth_date},{"field_name":"score","verbose_name":"امتیاز","value":self.score},{"field_name":"national_code","verbose_name":"کدملی یا شناسه ملی","value":self.national_code},{"field_name":"postal_code","verbose_name":"کدپستی","value":self.postal_code},{"field_name":"register_date","verbose_name":"تاریخ ثبت‌نام","value":self.register_date},{"field_name":"is_complete_information","verbose_name":"اطلاعات کامل است؟","value":self.is_complete_information},{"field_name":"is_active","verbose_name":"فعال/غیرفعال","value":self.is_active},{"field_name":"is_admin","verbose_name":"مدیر است؟","value":self.is_admin},{"field_name":"is_support","verbose_name":"پشتیبان است؟","value":self.is_support},{"field_name":"is_serviceman","verbose_name":"خدماتچی است؟","value":self.is_serviceman}]
    
    def show_short_image_profile(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="/media/{self.profile}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_profile.short_description = _("تصویر کاربر")
    def __str__(self):
        return f"{self.name} {self.family}"
    class Meta:
        verbose_name = _("کاربر سفارشی")
        verbose_name_plural = _("کاربران سفارشی")
        db_table ="table_custom_user"
    @property
    def is_staff(self):
        return self.is_admin
# end class CustomUser   
    
# start class Customer   
class Customer(models.Model):
    class_name = "Customer"
    user = models.OneToOneField(CustomUser, primary_key=True,on_delete=models.CASCADE,verbose_name=_("کاربر"))
    phone_number  = models.CharField(max_length=11,null=True, blank=True,verbose_name=_("شماره تماس"),help_text=_("شما تماسی است که وضعیت سفارش به آن ارسال می‌شود"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name=_("کشور"),null=True,help_text=_("کشوری که سفارش به آن ارسال شود"))
    state = models.ForeignKey(State, on_delete=models.CASCADE,verbose_name=_("استان یا ایالت"),null=True,help_text=_("استانی  که سفارش به آن ارسال شود"))
    city = models.ForeignKey(City, on_delete=models.CASCADE,verbose_name=_("شهر"),null=True,help_text=_("شهری که سفارش به آن ارسال می شود."))
    address = models.TextField(null=True, blank=True,verbose_name=_("آدرس"),help_text=_("آدرسی که می خواهید سفارش به آنجا ارسال شود"))
    latitude_location = models.CharField(max_length=15,blank=True,null=True,verbose_name=_("عرض جغرافیایی کاربر"))
    longitude_location = models.CharField(max_length=15,blank=True,null=True,verbose_name=_("طول جغرافیایی کاربر"))
    def fields_information(self):
        return [{"field_name":"user","verbose_name":"کاربر","value":self.user},{"field_name":"phone_number","verbose_name":"شماره تماس","value":self.phone_number},{"field_name":"country","verbose_name":"کشور","value":self.country},{"field_name":"state","verbose_name":"استان یا ایالت","value":self.state},{"field_name":"city","verbose_name":"شهر","value":self.city},{"field_name":"address","verbose_name":"آدرس","value":self.address}]
    def __str__(self):
        return f"{self.user}"
    class Meta:
        verbose_name = _("مشتری")
        verbose_name_plural = _("مشتریان")
        db_table ="table_customer"
# end class Customer   
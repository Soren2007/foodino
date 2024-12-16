# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField
# Create your models here.


class Gift(models.Model):
    title = models.CharField(max_length=80,verbose_name=_("عنوان هدیه"))
    description = models.TextField(verbose_name=_("توضیحات هدیه"))
    background_color = ColorField(verbose_name=_("رنگ پس زمینه"))
    color = ColorField(verbose_name=_("رنگ متن"))
    is_active = models.BooleanField(default=True,verbose_name=(_("فعال/غیرفعال")))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.title} - {self.description}"
    class Meta:
        verbose_name = _("هدیه")
        verbose_name_plural = _("هدایا")
        db_table ="table_gift"
 
class Lottery(models.Model):
    title = models.CharField(max_length=120,verbose_name=_("عنوان قرعه کشی"))
    image = models.ImageField(upload_to="images/gift/lottery/Lottery",verbose_name=_("بنر قرغه کشی"),help_text=_("لطفا غکس خود را بارگذاری کنید. نکته: بهتر است فرمت فایل بارگذاری شده webp باشد تا در سرعت سایت مشکلی پیش نیاید."))
    description = models.TextField(verbose_name=_("توضیحات قرعه کشی"))
    start_of_the_lottery = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ و زمان شروع قرعه کشی"))
    gifts = models.ManyToManyField(Gift,verbose_name=_("جایزه برنده"),help_text=_("کاربرانی که انتخاب میشوند این جایزه را هدیه می گیرند"))
    is_done = models.BooleanField(default=False,verbose_name= _("انجام شده؟"))
    is_start = models.BooleanField(default=False,verbose_name=_("مجوز شروع را دارد؟"))
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیرفعال"))
    user_number = models.PositiveIntegerField(default=1,verbose_name=_("تعداد کاربر"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = _("قرعه کشی")
        verbose_name_plural = _("قرعه کشی‌ها")
        db_table ="table_gift_lottery" 
        
class wheel_of_luck(models.Model):
    title = models.CharField(max_length=80,verbose_name=_("عنوان گردونه شانس"))
    description = models.TextField(verbose_name=_("توضیحات گردونه شانس"))
    max_user_score = models.PositiveIntegerField(default=30,verbose_name=_("حداقل امتیاز کاربر"))
    gifts = models.ManyToManyField(Gift,verbose_name=_("هدایا گردونه شانس"))
    is_active = models.BooleanField(default=True,verbose_name=(_("فعال/غیرفعال")))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.title} - {self.description}"
    class Meta:
        verbose_name = _("گردونه شانس")
        verbose_name_plural = _("گردونه‌های شانس")
        db_table ="table_gift_wheel_of_luck"
    
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.accounts.models import CustomUser
from apps.food.models import Food
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_mukbang_video(value):
    from os.path import splitext
    from django.core.exceptions import ValidationError
    ext = splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4','.mov','.webm']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('فرمت فایل انتخاب شده باید docx ، mp4 یا webm باشد.'))



class Mukbang(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, verbose_name=_("کاربر"))
    like = models.PositiveBigIntegerField(default=0,verbose_name=_("تعداد پستندیده‌ها"))
    dislike = models.PositiveBigIntegerField(default=0,verbose_name=_("تعداد نپستندیده‌ها"))
    views = models.PositiveBigIntegerField(default=0,verbose_name=_("تعداد بازدید"))
    share_number = models.PositiveBigIntegerField(default=0,verbose_name=_("تعداد اشتراک گذاشته شده"))
    video =  models.FileField(upload_to='videos/Mukbang/videos', verbose_name=_("ویدئو"), validators=[validate_mukbang_video])
    poster_image =  models.ImageField(upload_to='images/Mukbang/poster_image', verbose_name=_("تصویر پوستر"))
    food = models.ManyToManyField(Food, verbose_name=_("غذاها"))
    description = models.TextField(verbose_name=_("توضیحات"))
    register_date = models.DateField(verbose_name=_("تاریخ درج"),auto_now=True)
    is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return " "
    class Meta:
        verbose_name = _("موکبانگ")
        verbose_name_plural = _("موکبانگ‌ها")
        db_table ="table_mukbangs"
    
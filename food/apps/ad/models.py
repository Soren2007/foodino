# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Ad(models.Model):
    ACTION_MODEL = [("1",_("رنگ")),("2",_("لرزش")),("3",_("گردش")),("4",_("تار"))]
    ad_title = models.CharField(max_length=100,verbose_name=_("عنوان تبلیغ"),help_text=_("عنوان تبلیغ را وارد کنید."))
    ad_action_model = models.CharField(max_length=100,choices=ACTION_MODEL,default="1",help_text=_("شما می توانید یک انیمیشن را به متن رویداد اضافه کنید."),verbose_name=_("انیمیشن متن نمایشی"))
    ad_url = models.URLField(max_length=255,verbose_name=_("لینک انتقال صفحه"),help_text=_("لینکی است که با کلیک کردن کاربر بر روی آن کند آن صفحه باز میشود"))
    ad_image = models.ImageField(upload_to="images/ad/Ad/",verbose_name=_("بنر بتلیغ"),help_text=_("تصویری است که به کاربر نمایش داده میشود."))
    ad_start_date = models.DateField(auto_now_add=True,verbose_name=_("زمان شروع انتشار"),help_text=_("شما می توانید زمان انتشار را مشخص کنید."))
    ad_end_date = models.DateField(verbose_name=_("زمان پایان انتشار"),help_text=_("شما می توانید با تنظیم تاریخ پایان انتشار را مشخص کنید."))
    ad_is_active = models.BooleanField(verbose_name=_("فعال/غیرفعال"),default=False,help_text=_(""))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.ad_title}"
    def show_short_image_ad(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="/media/{self.ad_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_ad.short_description =_("بنر تبلیغ")
    class Meta:
        verbose_name = _("تبلیغ")
        verbose_name_plural = _("تبلیغات")
        db_table ="table_ads"
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from colorfield.fields import ColorField
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
# Create your models here.
ACTION_MODEL = [("1",_("رنگ")),("2",_("لرزش")),("3",_("گردش")),("4",_("تار"))]
class Event(models.Model):
    event_title = models.CharField(max_length=30,verbose_name=_("عنوان رویداد"))
    event_text = models.TextField(verbose_name=_("متن رویداد"))
    event_action_text = models.CharField(max_length=4,verbose_name="متن نمایشی")
    event_action_model = models.CharField(max_length=100,choices=ACTION_MODEL,default="1",help_text=_("شما می توانید یک انیمیشن را به متن رویداد اضافه کنید."),verbose_name=_("انیمیشن متن نمایشی"))
    event_image = models.ImageField(upload_to="images/event",verbose_name=_("تصویر رویداد"))
    event_register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    event_start_date = models.DateTimeField(verbose_name=_("تاریخ و زمان شروع رویداد"))
    event_end_date = models.DateTimeField(verbose_name=_("تاریخ و زمان پایان رویداد"))
    event_url = models.URLField(verbose_name=_("آدرس صفحه یا آدرس تارنما"))
    event_is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def show_short_image_event_image(self):
        return mark_safe(f'<img src="/media/{self.event_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_event_image.short_description = _("تصویر رویداد")
    def show_short_event_url(self):
        return mark_safe(f'<a href="{self.event_url}" dir="ltr" target="_blank">{self.event_url}</a>')
    show_short_event_url.short_description = _("لینک روداد")
    def __str__(self):
        return f"{self.event_title} {self.event_action_text}"
    class Meta:
        verbose_name = _("رویداد")
        verbose_name_plural = _("رویدادها")
        db_table ="table_events"
from datetime import date
class Top_Menu_Event(models.Model):
    event_title = models.CharField(max_length=300,verbose_name=_("عنوان رویداد"))
    event_title_color = ColorField(default='#FFF',format="hexa",verbose_name=_("رنگ متن"))
    event_action_text = models.CharField(max_length=100,verbose_name=_("متن نمایشی"))
    event_action_model = models.CharField(max_length=100,choices=ACTION_MODEL,default="1",help_text=_("شما می توانید یک انیمیشن را به متن رویداد اضافه کنید."),verbose_name=_("انیمیشن متن نمایشی"))
    event_image = models.ImageField(upload_to="images/top_menu_event",verbose_name=_("تصویر رویداد"))
    event_register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    event_start_date = models.DateField(verbose_name=_("تاریخ و زمان شروع رویداد"))
    event_end_date = models.DateField(verbose_name=_("تاریخ و زمان پایان رویداد"))
    event_url = models.URLField(verbose_name=_("آدرس صفحه یا آدرس تارنما"))
    event_is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def show_short_image_event_image(self):
        return mark_safe(f'<img src="/media/{self.event_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_event_image.short_description = _("تصویر رویداد")
    def show_short_event_url(self):
        return mark_safe(f'<a href="{self.event_url}" dir="ltr" target="_blank">{self.event_url}</a>')
    show_short_event_url.short_description = _("لینک روداد")
    def __str__(self):
        return f"{self.event_title} {self.event_action_text}"
    class Meta:
        verbose_name = _("رویداد بالای تارنما")
        verbose_name_plural = _("رویدادها بالای تارنما")
        db_table ="table_top_menu_events"
class Footer_Event(models.Model):
    event_title = models.CharField(max_length=300,verbose_name=_("عنوان رویداد"))
    event_action_text = models.CharField(max_length=100,verbose_name=_("متن نمایشی"))
    event_action_model = models.CharField(max_length=100,choices=ACTION_MODEL,default="1",help_text=_("شما می توانید یک انیمیشن را به متن رویداد اضافه کنید."),verbose_name=_("انیمیشن متن نمایشی"))
    event_start_date = models.DateTimeField(verbose_name=_("تاریخ و زمان شروع رویداد"))
    event_end_date = models.DateTimeField(verbose_name=_("تاریخ و زمان پایان رویداد"))
    event_url = models.URLField(verbose_name=_("آدرس صفحه یا آدرس تارنما"))
    event_is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def show_short_event_url(self):
        return mark_safe(f'<a href="{self.event_url}" dir="ltr" target="_blank">{self.event_url}</a>')
    show_short_event_url.short_description = _("لینک روداد")
    def __str__(self):
        return "{self.event_title} {self.event_action_text}"
    class Meta:
        verbose_name = _("رویداد پایین تارنما")
        verbose_name_plural = _("رویدادها پایین تارنما")
        db_table ="table_footer_events"

# File version
__version__ = "1.2.4"
# File Description
"""
this python file
"""
from django.db import models
from colorfield.fields import ColorField
from datetime import datetime
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

def validate_video_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.gif']
    if not ext.lower()  =='.gif':
        raise ValidationError(_('فایل انتخاب شده باید فرمت gif باشد.'))

# Create your models here.
SLID_TYPES=[('1',_('اسلاید ویدئویی')),('2',_('اسلاید تصویری'))]
class Slid(models.Model):
    slid_title = models.CharField(max_length=100,verbose_name=_("عنوان اسلاید"),help_text=_("شما می‌توانید برای اسلایدر عنوان مشخص کنید."))
    slid_color = ColorField(default='#FFF',format="hexa",verbose_name=_("رنگ متن عنوان"),help_text=_("شما می‌توانید رنگ عنوان را مشخص کنید."))
    slid_url = models.URLField(max_length=255,verbose_name=_("آدرس اسلاید"),help_text=_("آدرس صفحه‌ای که می‌خواهید با کلیک کاربر به آن صفحه هدایت شود."))
    slid_image = models.ImageField(upload_to="images/main/slider", null=True,blank=True,verbose_name=_("تصویر اسلاید"),help_text=_("تصویری که برای این اسلاید در نظر دارید را انتخاب کنید. نکته: بهتر است از عکس‌ با فرمت webp استفاده کنید."))
    slid_video = models.FileField(upload_to='videos/main/slider', null=True,blank=True, verbose_name=_("اسلاید ویدیویی"), validators=[validate_video_extension],help_text=_("در صورتی که می‌خواهید اسلاید متحرک باشد فایل gif(متحرک) خود را بارگذاری کنید. نکته: فرمت فایل باید gif باشد."))
    slid_type = models.CharField(max_length=100,choices=SLID_TYPES,verbose_name=_("نوع اسلاید"),help_text=_("نوع فایل بارگذاری شده را انتخاب کنید."))
    slid_start_date_time = models.DateTimeField(default=timezone.now,verbose_name=_("تاریخ و زمان شروع"))
    slid_end_date_time = models.DateTimeField(default=timezone.now,verbose_name=_("تاریخ و زمان پایان"))
    slid_register_date = models.DateTimeField(auto_now_add=True)
    slid_is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"),help_text=_("شما با فعال و یا غیرقعال کردن این گزینه می توانید وضعبت انتشار را مشخص کنید."))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.slid_title}"
    def show_short_image_slid(self):
        from django.utils.html import mark_safe
        if self.slid_type == '1':
            return mark_safe(f'<img src="/media/{self.slid_video}" style="width: 50px;height:50px;border-radius:50%">')
        return mark_safe(f'<img src="/media/{self.slid_image}" style="width: 50px;height:50px;border-radius:50%">')
    show_short_image_slid.short_description = _("تصویر اسلاید")
    class Meta:
        verbose_name = _("اسلاید")
        verbose_name_plural = _("اسلایدها")
        db_table ="table_slids"

class frequently_asked_question(models.Model):
    question = models.TextField(max_length=200,verbose_name=_("سوال"))
    response = RichTextUploadingField(max_length=500,verbose_name=_("پاسخ"))
    register_date = models.DateField(auto_now=True,verbose_name=_("تاریخ درج"))
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.question}"
    class Meta:
        verbose_name = _("سوال‌ متداول")
        verbose_name_plural = _("سوال‌های متداول")
        db_table ="table_frequently_asked_question"
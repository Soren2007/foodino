# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.accounts.models import CustomUser,Country
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Email(models.Model):
    MODS = [('1',_('ارسال به تمامی کاربران')),('2',_('ارسال به کاربران مشخص شده')),('3',_('ارسال به کاربران کشور')),('4',_('ارسال به مدیران')),("5",_("ارسال به پشتیبانان")),("6",_("ارسال به خدمات دهنده‌ها"))]
    subject = models.CharField(max_length=120,verbose_name=_("عنوان ایمیل"))
    message  = RichTextUploadingField(verbose_name=_("متن ایمیل"))
    mod =  models.CharField(max_length=120,verbose_name=_("حالت ایمیل"),choices=MODS)
    users = models.ManyToManyField(CustomUser,verbose_name=_("کاربران"),related_name="users")
    country = models.ManyToManyField(Country,verbose_name=_("کشورها"))
    register_date_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.subject} - {self.mod}"
    class Meta:
        verbose_name = _("ایمیل")
        verbose_name_plural = _("ایمیلها")
        db_table ="table_email"
    
    
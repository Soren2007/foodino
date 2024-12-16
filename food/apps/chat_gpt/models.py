# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.message.models import UserChatRoom
from django.utils.translation import gettext_lazy as _
# Create your models here.

class ChatGPT(models.Model):
    message = models.TextField(max_length=500,verbose_name=_("سوال پرسیده شده"))
    answer = models.TextField(verbose_name=_("پاسخ چت جی پی تی"))
    user = models.ForeignKey(UserChatRoom,verbose_name=_("کاربر"),on_delete=models.CASCADE)
    register_date = models.DateField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.user}"
    class Meta:
        verbose_name = _("هوش مصنوعی")
        verbose_name_plural = _("هوش مصنوعی")
        db_table ="table_Chat_GPT"
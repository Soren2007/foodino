# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from django.utils import timezone
from Middleware.middleware import RequestMiddleware
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Message(models.Model): 
    class_name = "Message"
    name = models.CharField(max_length=15,verbose_name=_("نام"))
    family = models.CharField(max_length=15,verbose_name=_("نام خانوادگی"))
    message = models.TextField(verbose_name=_("پیام"))
    email = models.EmailField(max_length=220,verbose_name=_("ایمیل"),null=True,blank=True)
    mobile_number = models.CharField(max_length=11,verbose_name=_("شماره موبایل"),help_text=_("شماره موبایل کاربر جدید را وارد کنید. نکته: شماره تماس کاربر نمی‌تواند تکراری باشد."))
    subject = models.CharField(max_length=300, verbose_name=_("عنوان"))
    is_seen = models.BooleanField(default=False, verbose_name=_("وضعیت دیده شده"))
    register_date = models.DateTimeField(default=timezone.now,verbose_name=_("تاریخ و زمان ثبت"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"name","verbose_name":'نام',"value":self.name},{"field_name":"family","verbose_name":'نام‌خانوادگی',"value":self.family},{"field_name":"message","verbose_name":'پیام',"value":self.message},{"field_name":"email","verbose_name":'ایمیل',"value":self.email},{"field_name":"subject","verbose_name":'عنوان',"value":self.subject},{"field_name":"register_date","verbose_name":'تاریخ درج',"value":self.register_date},{"field_name":"is_seen","verbose_name":'دیده شده؟',"value":self.is_seen}]
    def __str__(self):
        return f"{self.name} {self.family}"
    class Meta:
        verbose_name = _("پیام")
        verbose_name_plural = _("پیام ها")
        db_table ="table_messages"
    
class UserChatRoom(models.Model):
    class_name = "UserChatRoom"
    avatar_list = [('images/avatar/avatar_1.png',_('آواتار شماره یک')),('images/avatar/avatar_2.png',_('آواتار شماره دو')),('images/avatar/avatar_3.png',_('آواتار شماره سه')),('images/avatar/avatar_4.png',_('آواتار شماره چهار'))]
    full_name = models.CharField(max_length=120,verbose_name=_("نام و نام‌خانوادگی"))
    phone_number = models.CharField(max_length=11,verbose_name=_("شماره موبایل"), primary_key=True,unique=True)
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ ثبت‌نام"))
    avatar = models.CharField(choices=avatar_list,default='images/avatar/avatar_1.png',max_length=50,verbose_name=_("آواتار"))
    is_exist = models.BooleanField(default=False,verbose_name=_("ثبت شده؟"))
    is_support = models.BooleanField(default=False,verbose_name=_("پشتیببان است؟"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"full_name","verbose_name":'نام و نام‌خانوادگی',"value":self.full_name},{"field_name":"phone_number","verbose_name":'شماره موبایل',"value":self.phone_number},{"field_name":"register_date","verbose_name":'تاریخ درج',"value":self.register_date},{"field_name":"avatar","verbose_name":'آواتار',"value":self.avatar},{"field_name":"is_exist","verbose_name":'ثبت شده',"value":self.is_exist},{"field_name":"is_support","verbose_name":'پشتیبان است؟',"value":self.is_support}]
    def __str__(self):
        return f"{self.full_name}"
    class Meta:
        verbose_name = _("کاربر چت روم")
        verbose_name_plural = _("کاربران چت روم")
        db_table ="table_user_chat_room"

class ChatRoom(models.Model):
    class_name = "ChatRoom"
    sender_user = models.ForeignKey(UserChatRoom,on_delete=models.CASCADE,verbose_name=_("فرستنده"),related_name="message_user")
    receiver_user = models.ForeignKey(UserChatRoom,on_delete=models.CASCADE,verbose_name=_("گیرنده"),related_name="support_user",null=True,blank=True)
    message_text = models.TextField(verbose_name=_("متن پیام"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    message_parent = models.ForeignKey('ChatRoom',on_delete=models.CASCADE,verbose_name=_("والد پیام"),null=True,blank=True,related_name="message_child")
    is_seen = models.BooleanField(default=False, verbose_name=_("وضعیت دیده شده"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"sender_user","verbose_name":'کاربر فرسنتده',"value":self.sender_user},{"field_name":"receiver_user","verbose_name":'کاربر گیرنده',"value":self.receiver_user},{"field_name":"message_text","verbose_name":'متن پیام',"value":self.message_text},{"field_name":"message_text","verbose_name":'کاربر فرسنتده',"value":self.message_text},{"field_name":"register_date","verbose_name":'تاریخ درج',"value":self.register_date},{"field_name":"message_parent","verbose_name":'والد پیام',"value":self.message_parent}]
    def __str__(self):
        return f"{self.message_text}"
    def __iter__(self):
      yield {'sender_user':self.sender_user,'receiver_user':self.receiver_user,'message_text':self.message_text,'register_date':self.register_date}
    class Meta:
        verbose_name = _("چت روم")
        verbose_name_plural = _("چت روم")
        db_table ="table_chat_room"
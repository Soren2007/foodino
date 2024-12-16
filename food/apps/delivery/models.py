from django.db import models
from apps.accounts.models import CustomUser
from apps.branch.models import Branch
from django.utils.translation import gettext_lazy as _
# Create your models here.

class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=120,verbose_name=_("نام وسیله نقلیه"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.vehicle_type}"
    class Meta:
        verbose_name = _("نوع وشیله نقلیه")
        verbose_name_plural = _("انواع وسیله نقلیه")
        db_table ="table_vehicle_type"

def validate_profile_form(value):
    from os.path import splitext
    from django.core.exceptions import ValidationError
    ext = splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower()   in valid_extensions:
        raise ValidationError(_('فرمت فایل انتخاب شده باید pdf باشد.'))
   
class Delivery(models.Model):
    class_name = "Delivery"
    user = models.ForeignKey(CustomUser, verbose_name=_("کاربر"), on_delete=models.CASCADE)
    vehicle_type = models.OneToOneField(VehicleType,verbose_name=_("وسیله نقلیه"),on_delete=models.CASCADE)
    plaque = models.CharField(max_length=10, verbose_name=_("پلاک"))
    chassis_number = models.CharField(max_length=32,verbose_name=_("شماره شاسی"))
    profile_form = models.FileField(upload_to='files/delivery/profile_form', verbose_name=_("فایل فرم مشخصات"), validators=[validate_profile_form],help_text=_("لطفا فایل فرم مشخصات خود را بارگذاری کنید. نکته: فرمت فایل باید pdf  باشد."))
    ID_card_image = models.ImageField(upload_to='images/delivery/ID_card_image', verbose_name=_("تصویر کارت شناسایی"))
    branch = models.ForeignKey(Branch,verbose_name=_("شعبه‌ای که در آن فعالیت میکنند"),on_delete=models.CASCADE,null=True,blank=True)
    register_date = models.DateTimeField(auto_now=True,verbose_name=_("تاریخ درج"))
    your_last_activity = models.DateTimeField(auto_now=True,verbose_name=_("آخرین فعالیت شما"))
    is_accepted = models.BooleanField(default=False,verbose_name=_("تایید شده"))
    is_sending_the_order = models.BooleanField(default=False,verbose_name=_("درحال ارسال سفارش است؟"))
    is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        pass
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"user","verbose_name":_("کاربر"),"value":self.user},]
    def __str__(self):
        return f"{self.user}"
    class Meta:
        verbose_name = _("پیک")
        verbose_name_plural = _("پیک‌ها")
        db_table ="table_delivery"
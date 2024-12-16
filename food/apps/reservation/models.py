# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.accounts.models import CustomUser
from apps.food.models import Food
from apps.branch.models import Branch
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Reservation(models.Model):
    class_name = "Reservation"
    reservation_date_time = models.DateTimeField(verbose_name=_("زمان رزرو"))
    qr = models.CharField(max_length=100,verbose_name=_("کیو آر کد"))
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_("کاربری که رزرو کرده"))
    food = models.ManyToManyField(Food,verbose_name=_("غذاها"))
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name=_("شعبه"))
    description = models.TextField(verbose_name=_("توضحات"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"reservation_date_time","verbose_name":'زمان رزرو',"value":self.reservation_date_time},{"field_name":"qr","verbose_name":'qr image',"value":self.qr},{"field_name":"is_active","verbose_name":'فعال/غیرفعال',"value":self.is_active},{"field_name":"user","verbose_name":'کاربری که رزرو کرده است',"value":self.user},{"field_name":"food","verbose_name":'غذایی که رزرو کرده است',"value":self.food},{"field_name":"branch","verbose_name":'شعبه‌ای که رزرو کرده است',"value":self.branch}]
    def __str__(self):
        return f"{self.name} {self.family}"
    class Meta:
        verbose_name = _("رزرو")
        verbose_name_plural = _("رزروها")
        db_table ="table_reservation"
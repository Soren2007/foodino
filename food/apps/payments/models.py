# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.orders.models import Order
from apps.accounts.models import Customer
from apps.reservation.models import Reservation
from apps.accounts.models import Country
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.payment = models.ForeignKey(PaymentType,verbose_name=_("روش پرداخت"),default=None,on_delete=models.CASCADE,null=True,blank=True,related_name='PaymentTypes')


class Currency(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name=_("کشور"))
    currency = models.CharField(max_length=120,verbose_name=_("واحد پول"))
    ISO_code = models.CharField(max_length=5,verbose_name=_("کد ایزو"))
    symbol = models.CharField(max_length=30,verbose_name=_("علامت اختصاری"))
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.country}" 
    class Meta:
        verbose_name = _("واحد پول")
        verbose_name_plural = _("واحدهای پول")

class Payment(models.Model):
    class_name = "Payment"
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="payment_order",verbose_name=_("سفارش"),null=True,blank=True)
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE,null=True,blank=True,verbose_name=_("رزرو"))
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="payment_customer",verbose_name=_("مشتری"))
    register_date = models.DateTimeField(default=timezone.now,verbose_name=_("تاریخ پرداخت"))
    update_date = models.DateTimeField(auto_now=True,verbose_name=_("تاریخ ویرایش پرداخت"))
    amount = models.IntegerField(verbose_name=_("مبلغ پرداخت"))
    description = models.TextField(verbose_name=_("توضیحات پرداخت"))
    is_finally = models.BooleanField(default=False,verbose_name=_("وضعیت پرداخت"))
    status_code = models.IntegerField(verbose_name=_("کد وضعیت درگاه پرداخت"), null=True,blank=True)
    ref_id= models.CharField(max_length=36,verbose_name=_("شماره پیگیری پرداخت"), null=True,blank=True)
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"order","verbose_name":'سفارش',"value":self.order},{"field_name":"customer","verbose_name":'مشتری',"value":self.customer},{"field_name":"register_date","verbose_name":'تاریخ درج',"value":self.register_date},{"field_name":"update_date","verbose_name":'تاریخ آپدیت',"value":self.update_date},{"field_name":"amount","verbose_name":'مبلغ پرداخت',"value":self.amount},{"field_name":"description","verbose_name":'توضیحات',"value":self.description},{"field_name":"is_finally","verbose_name":'وضعیت پرداخت',"value":self.is_finally},{"field_name":"status_code","verbose_name":'کدوضعیت درگاه بانکی',"value":self.status_code},{"field_name":"ref_id","verbose_name":'شماره پیگیری پرداخت',"value":self.ref_id},]
    def __str__(self):
        return f"{self.order}"
    class Meta:
        verbose_name = _("پرداخت")
        verbose_name_plural = _("پرداخت‌ها")
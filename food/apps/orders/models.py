# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.accounts.models import Customer
from apps.food.models import Food,MyRecipes
from django.utils import timezone
from uuid import uuid4
from colorfield.fields import ColorField
# from utils import price_by_delivery_tax
from apps.subscription.models import Subscription
from apps.delivery.models import Delivery
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# Create your models here.
def price_by_delivery_tax(price,discount=0):
    delivery = 25000
    if price > 500000:
        delivery=0
    tax = (price+delivery)*0.09
    sum = price+delivery+tax
    sum = sum-(sum*discount/100)
    return int(sum),delivery,int(tax) 
class PaymentType(models.Model):
    class_name = "PaymentType"
    payment_title = models.CharField(max_length=50,verbose_name=_("نوع پرداخت"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"payment_title","verbose_name":'نوع پرداخت',"value":self.payment_title}]
    def __str__(self):
        return f"{self.payment_title}"
    class Meta:
        verbose_name = _("نوع پرداخت")
        verbose_name_plural = _("نواع روش پرداخت")
        


class OrderStatus(models.Model):
    order_status_title = models.CharField(_("عنوان وضعیت سفارش"),max_length=50,)
    def __str__(self) -> str:
        return f"{self.order_status_title}"
    class Meta:
       verbose_name = _("وضعیت سفارش")
       verbose_name_plural = _("انواع وضعیت‌های سفارش")
class Order(models.Model):
    class_name = "Order" 
    status_list = (("1",_("پردازش")),("2",_("آماده سازی سفارش")),("3",_("ارسال سفارش")),("4",_("تحویل داده شده")))
    register_date = models.DateTimeField(default=timezone.now,verbose_name=_('تاریخ درج سفارش'))
    update_date = models.DateTimeField(auto_now=True,verbose_name=_('تاریخ ویرایش سفارش'))
    is_finally = models.BooleanField(default=False,verbose_name=_('نهایی شده'))
    order_code = models.UUIDField(unique=True,default=uuid4,editable=False,verbose_name=_('کد تولیدی برای سفارش'))
    qr_code_image = models.ImageField(upload_to="images/order/qr_code/",verbose_name=_('کیوآرکد برای سفارش'),null=True,blank=True)
    qr_code_color = ColorField(default="#ff5000",format="hexa",verbose_name=_('کد تولیدی برای سفارش'))
    discount = models.IntegerField(default=0,verbose_name=_('تخفیف'),null=True,blank=True)
    description = models.TextField(null=True,blank=True,verbose_name=_("توضیحات"))
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orders',verbose_name=_('مشتری '))
    status = models.ForeignKey(OrderStatus,on_delete=models.CASCADE,verbose_name=_("وضعیت سفارش"),related_name="orders_order_status",null=True,blank=True)
    payment = models.ForeignKey(PaymentType,verbose_name=_("روش پرداخت"),default=None,on_delete=models.CASCADE,null=True,blank=True,related_name='PaymentTypes')
    delivery = models.ForeignKey(Delivery,verbose_name=_("پیک"),on_delete=models.CASCADE,null=True,blank=True)
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"customer","verbose_name":'مشتری',"value":self.customer},{"field_name":"register_date","verbose_name":'تاریخ درج',"value":self.register_date},{"field_name":"update_date","verbose_name":'تاریخ آپدیت',"value":self.update_date},{"field_name":"is_finally","verbose_name":'نهایی شده؟',"value":self.is_finally},{"field_name":"status","verbose_name":'وضعیت سفارش',"value":self.status},{"field_name":"order_code","verbose_name":'کدتولیدی برای سفارش',"value":self.order_code},{"field_name":"discount","verbose_name":'تخفیف',"value":self.discount},{"field_name":"description","verbose_name":'توضیحات',"value":self.description},{"field_name":"payment","verbose_name":'روش پرداخت',"value":self.payment},]
    def get_order_total_price(self):
        sum=0
        for item in self.orders_details1.all():
            if item.food:
                sum+=item.food.get_price_by_discount()*item.qty
            else:
                sum+=item.my_recipes.get_price_by_discount()*item.qty
        order_final_price,delivery,tax=price_by_delivery_tax(sum,self.discount)
        return int(order_final_price)
         
    def __str__(self):
        return f"{self.customer}"
    class Meta:
        verbose_name = _("سفارش")
        verbose_name_plural = _("سفارشات")

how_to_use = [("1", "ارسال مواد خام به همراه دستور غذاها"), ("2","ارسال غذاها پخته شده"),("3","رزور غذاها")]
class OrderDetails(models.Model):
    class_name = "OrderDetails"
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orders_details1',verbose_name=_('سفارش'))
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name='orders_details2',verbose_name=_('غذا'),null=True,blank=True)
    my_recipes = models.ForeignKey(MyRecipes,on_delete=models.CASCADE,related_name='orders_details3',verbose_name=_('دستور غذایی کاربر'),null=True,blank=True)
    qty = models.PositiveBigIntegerField(verbose_name=_('تعداد'),default=1)
    price = models.IntegerField(verbose_name=_('قیمت'))
    how_to_use = models.CharField(max_length=120,verbose_name=_("چگونگی مصرف"),choices=how_to_use,default="2")
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"order","verbose_name":'سفارش',"value":self.order},{"field_name":"food","verbose_name":'غذایی که سفارش داده شده',"value":self.food},{"field_name":"my_recipes","verbose_name":'دستور غذایی که سفارش داده شده',"value":self.my_recipes},{"field_name":"qty","verbose_name":'تعداد',"value":self.qty},{"field_name":"price","verbose_name":'قیمت',"value":self.price},]
    def __str__(self):
        return f"{self.order}"
class OrderDetailsSubscription(models.Model):
    class_name = "OrderDetailsSubscription"
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orders_details_subscription',verbose_name=_('سفارش'))
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.order}"
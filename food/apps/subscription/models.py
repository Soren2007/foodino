# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.accounts.models import CustomUser
from apps.food.models import Food,MyRecipes
from django.utils.translation import gettext_lazy as _
# Create your models here.

# version
__version__ = "1.1.1"
"""
this python file
"""

class Promise(models.Model):
    DAYS_OF_WEEK = [('1',_("شنبه")),('2',_("یک‌شنبه")),('3',_("دوشنبه")),('4',_("سه‌شنبه")),('5',_("چهارشنبه")),('6',_("پنج‌شنبه")),('7',_("جمعه")),]
    foods = models.ManyToManyField(Food,verbose_name=_("غذاهای وعده"))
    my_recipes = models.ManyToManyField(MyRecipes,verbose_name=_("غذاهای وعده"))
    user = models.ForeignKey(CustomUser,verbose_name=_("کاربر"),on_delete=models.CASCADE)   
    promise_time = models.TimeField(verbose_name=_("تایین زمان ارسال وعده"))
    day_of_week = models.CharField(verbose_name=_("روز هفته"),max_length=100,choices=DAYS_OF_WEEK)
    description = models.TextField(verbose_name=_("توضحات"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیرفعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.user} - {self.is_active}"
    class Meta:
        verbose_name = _("وعده غذایی کاربر")
        verbose_name_plural = _("وعده های غذایی کاربر")
        db_table ="table_promise"
        
class Subscription(models.Model):
    subscription_title = models.CharField(verbose_name=_("عنوان اشتراک"),default="یک ماهه",max_length=50)
    subscription_price = models.PositiveIntegerField(verbose_name=_("قیمت اشتراک"),default=200000)
    subscription_discount = models.PositiveIntegerField(verbose_name=_("تخفیف به تومان"),default=200000)
    is_special_for_new_users = models.BooleanField(default=True,verbose_name=_("ویؤه کاربران جدید است؟"))
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیر فعال"))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def __str__(self):
        return f"{self.subscription_title}"
    class Meta:
        verbose_name = _("اشتراک کاربر")
        verbose_name_plural = _("اشتراک های کاربر")
        db_table ="table_subscription_user"
        
class SubscriptionUser(models.Model):
    subscription = models.ForeignKey(Subscription,verbose_name=_("اشتراکی که فعال شده است."),on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,verbose_name=_("کاربر"),on_delete=models.CASCADE)
    promise = models.ManyToManyField(Promise,verbose_name=_("وعده های غذایی"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیر فعال"))
    def __str__(self):
        return f"{self.user}"
    class Meta:
        verbose_name = _("اشتراک")
        verbose_name_plural = _("اشتراک")
        db_table ="table_subscription"
    
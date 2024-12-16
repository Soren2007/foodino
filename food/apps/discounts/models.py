# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.food.models import Food,MyRecipes
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Coupon(models.Model):
    class_name = "Coupon"
    coupon_code  = models.CharField(max_length=10,unique=True,verbose_name=_("کد کوپن"))
    start_date = models.DateTimeField(verbose_name=_('تاریخ شروع'))
    end_date = models.DateTimeField(verbose_name=_('تاریخ پایان'))
    discount = models.IntegerField(verbose_name=_('درصد تخفیف'),validators=[MinValueValidator(0),MaxValueValidator(100)])
    allowed_number_used = models.IntegerField(verbose_name=_("تعداد مجاز استفاده شده"),default=1,null=True,blank=True)
    number_used = models.IntegerField(verbose_name=_("تعداد استفاده شده"),default=0,null=True,blank=True)
    is_active = models.BooleanField(default=False,verbose_name=_('وضعیت فعال/غیرفعال'))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"coupon_code","verbose_name":'کد بن تخفیف',"value":self.coupon_code},{"field_name":"start_date","verbose_name":"تاریخ شروع بن تخفیف","value":self.start_date},{"field_name":"end_date","verbose_name":"تاریخ پایان بن تخفیف","value":self.end_date},{"field_name":"discount","verbose_name":"درصد تخفیف","value":self.discount},{"field_name":"is_active","verbose_name":"فعال/غیرفعال","value":self.is_active}]
    def __str__(self):
        return f"{self.coupon_code}"
    class Meta:
        verbose_name = _("بن تخفیف")
        verbose_name_plural = _("بن تخفیف‌ها")
class DiscountBasket(models.Model):
    class_name = "DiscountBasket"
    discount_title = models.CharField(max_length=100,verbose_name=_('عنوان سبد تخفیف'))
    start_date = models.DateTimeField(verbose_name=_('تاریخ شروع'))
    end_date = models.DateTimeField(verbose_name=_('تاریخ پایان'))
    discount = models.IntegerField(verbose_name=_('درصد تخفیف'),validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active = models.BooleanField(default=False,verbose_name=_('وضعیت فعال/غیرفعال'))
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"discount_title","verbose_name":'عنوان تخفیف',"value":self.discount_title},{"field_name":"start_date","verbose_name":"تاریخ شروع بن تخفیف","value":self.start_date},{"field_name":"end_date","verbose_name":"تاریخ پایان تخفیف","value":self.end_date},{"field_name":"discount","verbose_name":"درصد تخفیف","value":self.discount},{"field_name":"is_active","verbose_name":"فعال/غیرفعال","value":self.is_active}]
    def __str__(self):
        return f"{self.discount_title}"
    class Meta:
        verbose_name = _("سبد تخفیف")
        verbose_name_plural = _("سبدهای تخفیف")
class DiscountBasketDetail(models.Model):
    class_name = "DiscountBasketDetail"
    discount_basket = models.ForeignKey(DiscountBasket,on_delete=models.CASCADE,verbose_name="سبد تخفیف", related_name="discount_basket_detail_1")
    food = models.ForeignKey(Food,on_delete=models.CASCADE,verbose_name="غذا",related_name="food_discount_basket_detail_2",null=True)
    my_recipe = models.ForeignKey(MyRecipes,on_delete=models.CASCADE,verbose_name=_("غذای کاربر"),related_name="my_recipe_discount_basket_detail_2",null=True)
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"discount_basket","verbose_name":'سبد تخفیف',"value":self.discount_basket},{"field_name":"food","verbose_name":"غذایی که تخفیف دارد","value":self.food},{"field_name":"my_recipe","verbose_name":"دستور غذایی که تخفیف دارد","value":self.my_recipe}]
    def __str__(self):
        return f"{self.discount_basket}"
    class Meta:
        verbose_name = _("جزء سبد تخفیف")
        verbose_name_plural = _("جزئیات سبد تخفیف")
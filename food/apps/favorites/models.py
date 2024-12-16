# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.food.models import Food
from apps.accounts.models import CustomUser
from apps.blog.models import Article
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Favorite(models.Model):
    class_name = "Favorite"
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name="favorite_food",verbose_name=_("غذا"))
    favorite_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="favorite_user",verbose_name=_("کاربر علاقه مند"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"food","verbose_name":'فذا مورد علاقه',"value":self.food},{"field_name":"favorite_user","verbose_name":"کاربری که غذا را به علافه خود افزوده است","value":self.favorite_user},{"field_name":"register_date","verbose_name":"تاریخ درج","value":self.register_date}]
    def __str__(self):
        return f"{self.food} - {self.favorite_user}"
    class Meta:
        verbose_name = _("غذای مورد علاقه")
        verbose_name_plural = _("غذاهای مورد علاقه")
         
class Favorite_Blog(models.Model):
    class_name = "Favorite_Blog"
    blog = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="favorite_blog",verbose_name=_("مقاله"))
    favorite_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="favorite_blog_user",verbose_name=_("کاربر علاقه مند"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"blog","verbose_name":'مقاله مورد علاقه',"value":self.blog},{"field_name":"favorite_user","verbose_name":"کاربری که غذا را به علافه خود افزوده است","value":self.favorite_user},{"field_name":"register_date","verbose_name":"تاریخ درج","value":self.register_date}]
    def __str__(self):
        return f"{self.blog} - {self.favorite_user}"
    class Meta:
        verbose_name = _("مقاله‌ی مورد علاقه")
        verbose_name_plural = _("مقاله‌های مورد علاقه")

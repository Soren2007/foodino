# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.food.models import Food,Recipes
from apps.accounts.models import CustomUser
from apps.blog.models import Article
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Comment(models.Model): 
    class_name = "Comment"
    food=models.ForeignKey(Food,on_delete=models.CASCADE,verbose_name=_("غذا"),related_name="comments_food",null=True,blank=True)
    recipes=models.ForeignKey(Recipes,on_delete=models.CASCADE,verbose_name=_("دستور"),related_name="comments_recipes",null=True,blank=True)
    blog=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name=_("مقاله"),related_name="comments_blog",null=True,blank=True)
    commenting_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_("کاربر نظر دهنده"),related_name="comment_user_1")
    approving_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_("کاربر تایید کننده نظر"),related_name="comment_user_2",null=True,blank=True)
    comment_text = models.TextField(verbose_name=_("متن نظر"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    is_active = models.BooleanField(default=False,verbose_name=_("وضعیت نظر"))
    comment_parent = models.ForeignKey('Comment',on_delete=models.CASCADE,verbose_name=_("والد نظر"),null=True,blank=True,related_name="comments_child")
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"food","verbose_name":'غذایی که در آن کامنت داده شده',"value":self.food},{"field_name":"recipes","verbose_name":"دستور غذایی که در آن کامنت داده شده","value":self.recipes},{"field_name":"blog","verbose_name":"مقاله‌ای که در آن کامنت داده شده","value":self.blog},{"field_name":"commenting_user","verbose_name":"کاربر نظر دهنده","value":self.commenting_user},{"field_name":"approving_user","verbose_name":"کاربر نظر تایید کننده","value":self.approving_user},{"field_name":"comment_text","verbose_name":"متن نظر","value":self.comment_text},{"field_name":"register_date","verbose_name":"تاریخ درج نظر","value":self.register_date},{"field_name":"is_active","verbose_name":"فعال/غیرفعال","value":self.is_active},{"field_name":"comment_parent","verbose_name":"والد نظر","value":self.comment_parent}]
    def __str__(self):
        return f"{self.food} - {self.commenting_user}"
    class Meta:
        verbose_name = _("نظر")
        verbose_name_plural = _("نظرات")
        
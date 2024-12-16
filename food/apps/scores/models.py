# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.food.models import Food
from apps.accounts.models import CustomUser
from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Scoring(models.Model):
    class_name = "Scoring"
    food = models.ForeignKey(Food,on_delete=models.CASCADE,related_name="scoring_food",verbose_name=_("غذا"))
    scoring_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="scoring_user",verbose_name=_("امتیاز دهنده"))
    register_date = models.DateTimeField(auto_now_add=True,verbose_name=_("تاریخ درج"))
    score = models.PositiveSmallIntegerField(validators=[MinLengthValidator(0),MaxLengthValidator(5)],verbose_name=_("امتیاز"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"food","verbose_name":'غذایی که کاربرر به آن امتیاز داده است',"value":self.food},{"field_name":"scoring_user","verbose_name":'کاربری که امتیاز داده است',"value":self.scoring_user},{"field_name":"register_date","verbose_name":'تاریخ درج امتیاز',"value":self.register_date},{"field_name":"score","verbose_name":'امتیاز',"value":self.score}]
    def __str__(self):
        return f"{self.food} - {self.scoring_user}"
    class Meta:
        verbose_name = _("امتیاز")
        verbose_name_plural = _("امتیازات")
        
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from apps.accounts.models import CustomUser,Country,State,City
from django.utils.translation import gettext_lazy as _
# Create your models here.

class robot_takes_containers(models.Model):
    model = models.CharField(max_length=150,verbose_name=_("مدل ربات"))
    country_location = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name=_("کشوری که ربات در آن فعاللیت می‌کند"))
    state_location = models.ForeignKey(State,on_delete=models.CASCADE,verbose_name=_("استانی که ربات در آن فعاللیت می‌کند"))
    city_location = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name=_("شهری که ربات در آن فعاللیت می‌کند"))
    google_map_location_link = models.TextField(verbose_name=_("آدرس گوگل مپ ربات"),blank=True,null=True)
    is_active = models.BooleanField(default=False,verbose_name=_("فعال/غیرفعال"))
    def __str__(self):
        return f"{self.model} - {self.country_location} - {self.city_location}"
    class Meta:
        verbose_name = _("ربات گیرنده ظروف")
        verbose_name_plural = _("ربات‌های گیرینده ظروف")
        db_table ="table_robot_takes_containers"
 
class my_environment(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_("کاربری که ظروف را به دست گاه تحویل داده است"))
    number_dishes = models.PositiveIntegerField(default=0,verbose_name=_("تعداد ظروفی که کاربر به دستگاه داده است"))
    points_unit = models.PositiveIntegerField(default=50,verbose_name=_("واحد امتیاز"))
    robot_takes = models.ForeignKey(robot_takes_containers,on_delete=models.CASCADE,verbose_name=_("رباتی که ظروف را گرفته"))
    def __str__(self):
        return f"{self.user} - {self.number_dishes} - {self.points_unit}"
    class Meta:
        verbose_name = _("کاربر محیط زیستی")
        verbose_name_plural = _("کاربران محیط زیستی")
        db_table ="table_my_environment"
    
        
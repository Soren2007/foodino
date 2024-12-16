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

class Branch(models.Model):
    class_name = "Branch" 
    branch_name = models.CharField(max_length=180,verbose_name=_("نام شعبه"),help_text=_("نام شعبه را به صورت فارسی وارد کنید."))
    branch_number = models.IntegerField(verbose_name=_("شماره شعبه"),help_text=_("شماره شعبه در کشور خود را وارد کنید."))
    branch_capacity = models.IntegerField(verbose_name=_("ظرفیت شعبه"))
    branch_number_of_tables = models.IntegerField(verbose_name=_("تعداد میزهای شعبه"))
    branch_address = models.TextField(verbose_name=_("آدرس شعبه"))
    branch_google_map_link = models.URLField(verbose_name=_("لیتک گوگل مپ"),null=True,blank=True)
    branch_3d_map_link = models.URLField(verbose_name=_("نقشه سه بعدی شعبه"),null=True,blank=True)
    branch_country = models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name=_("کشوری که در آن خدمات اراعه می کنید."))
    branch_state = models.ForeignKey(State,on_delete=models.CASCADE,verbose_name=_("استان یا ایالتی که در آن خدمات اراعه می کنید."))
    branch_city = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name=_("شهری که در آن خدمات اراعه می کنید."))
    branch_manager = models.ForeignKey(CustomUser,on_delete=models.CASCADE,verbose_name=_("مدیر شعبه"))
    is_active = models.BooleanField(verbose_name=_("وضعیت"),default=False)
    is_translated_content = models.BooleanField(default=False,verbose_name=_("آیا محتوا ترجمه شده؟"))
    def fields_information(self):
        return [{"field_name":"id","verbose_name":'id',"value":self.id},{"field_name":"branch_name","verbose_name":'نام شعبه',"value":self.branch_name},{"field_name":"branch_number","verbose_name":"شماره شعبه","value":self.branch_number},{"field_name":"branch_capacity","verbose_name":"ظرفیت شعبه","value":self.branch_capacity},{"field_name":"branch_number_of_tables","verbose_name":"شماره شعبه","value":self.branch_number_of_tables},{"field_name":"branch_address","verbose_name":"تعداد میز شعبه","value":self.branch_address},{"field_name":"branch_google_map_link","verbose_name":"آدرس شعبه","value":self.branch_google_map_link},{"field_name":"branch_3d_map_link","verbose_name":"لینک گوگل مپ شعبه","value":self.branch_3d_map_link},{"field_name":"branch_country","verbose_name":"نقشه سه بعدی شعبه شعبه","value":self.branch_country},{"field_name":"branch_state","verbose_name":"کشور شعبه","value":self.branch_state},{"field_name":"branch_city","verbose_name":"استان یا ایالت شعبه","value":self.branch_city},{"field_name":"branch_manager","verbose_name":"شهر شعبه","value":self.branch_manager},{"field_name":"is_active","verbose_name":"فعال/غیرفعال","value":self.is_active}]
    def __str__(self):
        return f"{self.branch_name}"
    class Meta:
        verbose_name = _("شعبه")
        verbose_name_plural = _("شعب")
        db_table ="table_branches"
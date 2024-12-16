# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.

class Language(models.Model):
    language_code = models.CharField(max_length=20,verbose_name=_("کد زبان"))
    language_name = models.CharField(max_length=120,verbose_name=_("نام زبان به انگلیسی"))
    language_directionality = models.CharField(max_length=120,verbose_name=_("راست چین یا چپ چین زبان"),default='rtl')
    language_is_active = models.BooleanField(default=False,verbose_name=_("قعال/غیرفعال"))
    def __str__(self):
        return f"{self.language_code} - {self.language_name}"
    class Meta:
        verbose_name = _("زبان")
        verbose_name_plural = _("زبان‌ها")
        db_table ="table_languages"

def validate_language_font_font_file_embedded_opentype(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.eot']
    if not ext.lower()  =='.eot':
        raise ValidationError(_('فایل انتخاب شده باید فرمت .eot باشد.'))
    
def validate_language_font_font_file_truetype(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.eot']
    if not ext.lower()  =='.eot':
        raise ValidationError(_('فایل انتخاب شده باید فرمت .ttf باشد.'))
    
def validate_language_font_font_file_woff(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.woff']
    if not ext.lower()  =='.woff':
        raise ValidationError(_('فایل انتخاب شده باید فرمت .woff باشد.'))
    
def validate_language_font_font_file_woff_2(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.woff2']
    if not ext.lower()  =='.woff2':
        raise ValidationError(_('فایل انتخاب شده باید فرمت .woff2 باشد.'))

def set_font_file_name(language,font_name,format):
    return f"{settings.BASE_DIR}/static/fonts"
# /{language.language_code}/{font_name}.{format}
   
class LanguageFont(models.Model):
    font_name = models.CharField(max_length=100,verbose_name=_("نام فونت"))
    
    language = models.ForeignKey(Language,verbose_name=_("زبان"),on_delete=models.CASCADE)
    
    font_embedded_opentype_format = models.FileField(upload_to=set_font_file_name(language,font_name,'eot'), null=True,blank=True, verbose_name=_("افایل فونت .eot"), validators=[validate_language_font_font_file_embedded_opentype],help_text=_("s"))
    
    font_truetype_format = models.FileField(upload_to=set_font_file_name(language,font_name,'ttf'), null=True,blank=True, verbose_name=_("افایل فونت .ttf"), validators=[validate_language_font_font_file_truetype],help_text=_("s"))
    
    font_woff_format = models.FileField(upload_to=set_font_file_name(language,font_name,'woff'), null=True,blank=True, verbose_name=_("افایل فونت .woff"), validators=[validate_language_font_font_file_woff],help_text=_("s"))
    
    font_woff_2_format = models.FileField(upload_to=set_font_file_name(language,font_name,'woff2'), null=True,blank=True, verbose_name=_("افایل فونت .woff"), validators=[validate_language_font_font_file_woff_2],help_text=_("s"))
    
    is_active = models.BooleanField(default=True,verbose_name=_("فعال/غیرفعال"))
    
    def __str__(self):
        return f"{self.language}"
    class Meta:
        verbose_name = _("فونت")
        verbose_name_plural = _("فونت‌ها")
        db_table ="table_languages_fonts"
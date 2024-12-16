# version
__version__ = "1.1.1"
"""
this python file
"""

from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_ad","ad_title","ad_url","ad_start_date","ad_end_date",'is_translated_content',"ad_is_active")
    search_fields = ("ad_title","ad_url","ad_start_date","ad_end_date",'is_translated_content',"ad_is_active")
    readonly_fields= ('show_short_image_ad',)
    list_editable = ('is_translated_content',"ad_is_active",)
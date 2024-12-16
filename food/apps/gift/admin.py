# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Gift)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ("title","description","color","background_color",'is_translated_content',"is_active")
    list_filter = ("title","description","color","background_color","is_active")
    search_fields = ("title","description","color","background_color","is_active")
    list_editable = ('is_translated_content',"is_active",)

@admin.register(Lottery)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ("title","is_start","start_of_the_lottery",'is_translated_content',"is_start","is_active")
    list_filter = ("title","is_start","start_of_the_lottery","is_active")
    search_fields = ("title","is_start","start_of_the_lottery","is_active")
    filter_horizontal=('gifts',)
    list_editable = ('is_translated_content',"is_active","is_start")
    
@admin.register(wheel_of_luck)
class LotteryAdmin(admin.ModelAdmin):
    list_display = ("title","description","max_user_score",'is_translated_content',"is_active")
    list_filter = ("title","description","max_user_score","is_active")
    search_fields = ("title","description","max_user_score","is_active")
    filter_horizontal=('gifts',)
    list_editable = ('is_translated_content',"is_active",)
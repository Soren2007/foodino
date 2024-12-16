# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Slid)
class slidAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_slid","slid_title",'is_translated_content',"slid_is_active")
    search_fields = ("slid_title",)
    readonly_fields = ("show_short_image_slid",)
    list_editable = ('is_translated_content',"slid_is_active",)
@admin.register(frequently_asked_question)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ("question","register_date",'is_translated_content',"is_active")
    search_fields = ("question","response")
    list_editable = ('is_translated_content',"is_active",)
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_event_image","event_title","event_text","event_register_date","event_start_date","event_end_date","show_short_event_url",'is_translated_content',"event_is_active")
    search_fields = ("event_title","event_text","event_image","event_register_date","event_start_date","event_end_date","event_url","event_is_active")
    list_filter = ("event_title",)
    list_editable = ("event_is_active",'is_translated_content',)
    readonly_fields = ("show_short_image_event_image","show_short_event_url",)
@admin.register(Top_Menu_Event)
class Top_Menu_EventAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_event_image","event_title","event_title_color","event_register_date","event_start_date","event_end_date","show_short_event_url",'is_translated_content',"event_is_active")
    search_fields = ("event_title","event_title_color","event_image","event_register_date","event_start_date","event_end_date","event_url","event_is_active")
    list_editable = ('is_translated_content',"event_is_active",)
    list_filter = ("event_title",) 
    readonly_fields = ("show_short_image_event_image","show_short_event_url",)
@admin.register(Footer_Event)
class Footer_EventAdmin(admin.ModelAdmin):
    list_display = ("event_title","event_start_date","event_end_date","show_short_event_url",'is_translated_content',"event_is_active")
    search_fields = ("event_title","event_start_date","event_end_date","event_url","event_is_active")
    list_filter = ("event_title",)
    list_editable = ('is_translated_content',"event_is_active",)
    readonly_fields = ("show_short_event_url",)
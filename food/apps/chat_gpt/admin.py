# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import ChatGPT
# Register your models here.


@admin.register(ChatGPT)
class ChatGPTAdmin(admin.ModelAdmin):
    list_display = ("user","message",'is_translated_content')
    search_fields = ("user","message","answer")
    raw_id_fields = ("user",)
    ordering = ("register_date",)
    list_editable = ('is_translated_content',)
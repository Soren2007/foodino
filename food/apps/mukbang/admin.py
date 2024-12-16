# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import Mukbang
# Register your models here.

@admin.register(Mukbang)
class MukbangAdmin(admin.ModelAdmin):
    list_display = ("user","video","like","dislike","register_date",'is_translated_content')
    list_filter = ("user","like","dislike","register_date")
    search_fields = ("user","video","like","dislike","register_date")
    list_editable = ('is_translated_content',)
    raw_id_fields = ("user",)
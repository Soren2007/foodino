# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Language)
class languageAdmin(admin.ModelAdmin):
    list_display = ("language_code","language_name","language_directionality","language_is_active")
    search_fields = ("language_code","language_name","language_directionality","language_is_active")
    list_editable = ("language_is_active",)

@admin.register(LanguageFont)
class LanguageFontAdmin(admin.ModelAdmin):
    list_display = ("font_name","language","is_active")
    search_fields = ("font_name","language","is_active")
    list_editable = ("is_active",)
    raw_id_fields = ("language",)
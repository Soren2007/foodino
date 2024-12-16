# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("order","customer","register_date","update_date","amount","description","is_finally","status_code","ref_id",'is_translated_content')
    search_fields = ("order","customer","register_date","update_date","amount","description","is_finally","status_code","ref_id")
    list_filter = ("order","customer","register_date","update_date","amount","is_finally","status_code")
    raw_id_fields = ("order","reservation","customer")
    list_editable = ('is_translated_content',)
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("country","currency","ISO_code","symbol",'is_translated_content',"is_active")
    search_fields = ("currency",)
    list_filter = ("ISO_code","symbol","is_active")
    raw_id_fields = ("country",)
    list_editable = ('is_translated_content',"is_active") 
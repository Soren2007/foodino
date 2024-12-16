# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

class OrderDetailsInLine(admin.TabularInline):
    model = OrderDetails
    raw_id_fields = ("order","food","my_recipes")
    extra = 3

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ("payment_title",'is_translated_content',)
    list_filter = ("payment_title",)
    search_fields = ("payment_title",)
    list_editable = ('is_translated_content',)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("customer","register_date","is_finally","discount",'is_translated_content',)
    list_filter = ("customer","register_date","is_finally","discount")
    search_fields = ("customer","register_date","is_finally","discount")
    inlines = [OrderDetailsInLine]
    raw_id_fields = ("customer","status","payment","delivery")
    list_editable = ('is_translated_content',)
@admin.register(OrderStatus)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_status_title",)
    list_filter = ("order_status_title",)
    search_fields = ("order_status_title",)
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("coupon_code","start_date","end_date","discount","is_active")
    list_filter = ("coupon_code","start_date","end_date","discount","is_active")
    search_fields = ("coupon_code","start_date","end_date","discount","is_active")
    ordering = ('is_active',)
    list_editable = ("is_active",)
    
class DiscountBasketDetailsInline(admin.TabularInline):
    model = DiscountBasketDetail
    raw_id_fields = ("discount_basket","food","my_recipe")
    extra = 3
@admin.register(DiscountBasket)
class DiscountBasketAdmin(admin.ModelAdmin):
    list_display = ("discount_title","start_date","end_date","discount",'is_translated_content',"is_active")
    list_filter = ("discount_title","start_date","end_date","discount","is_active")
    search_fields = ("discount_title","start_date","end_date","discount","is_active")
    ordering = ('is_active',)
    list_editable = ('is_translated_content',"is_active",)
    inlines = [DiscountBasketDetailsInline]
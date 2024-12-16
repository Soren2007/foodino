# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ("vehicle_type",'is_translated_content')
    search_fields = ("vehicle_type",)
    list_editable = ('is_translated_content',)
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("user","vehicle_type","plaque","register_date","is_sending_the_order",'is_translated_content',"is_active")
    list_filter = ("user","vehicle_type","plaque","register_date","is_sending_the_order")
    search_fields = ("user","vehicle_type","plaque","register_date","is_sending_the_order","is_active")
    ordering = ("is_active",)
    raw_id_fields = ("user","branch")
    list_editable = ('is_translated_content',"is_active",)
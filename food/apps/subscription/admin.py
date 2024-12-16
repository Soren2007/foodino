# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
# Register your models here.


__version__ = "1.1.1"

@admin.register(Promise)
class PromiseAdmin(admin.ModelAdmin):
    list_display = ('id','is_translated_content',"is_active",)
    search_fields = ("is_active",)
    list_filter = ("is_active",)
    list_editable = ('is_translated_content',"is_active",)
    
@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("subscription_title","subscription_price",'is_translated_content',"is_active","is_special_for_new_users")
    search_fields = ("subscription_title","subscription_price","is_active","is_special_for_new_users")
    list_filter = ("subscription_title","subscription_price","is_active","is_special_for_new_users")
    list_editable = ('is_translated_content',"is_active","is_special_for_new_users")
    
@admin.register(SubscriptionUser)
class SubscriptionUserAdmin(admin.ModelAdmin):
    list_display = ("register_date","is_active")
    search_fields = ("register_date","is_active")
    list_filter = ("register_date","is_active")
    # list_editable = ("is_active",)
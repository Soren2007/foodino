# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("branch_name","branch_number","branch_capacity","branch_number_of_tables","branch_google_map_link","branch_country","branch_state","branch_city",'is_translated_content',"is_active")
    search_fields= ("branch_name","branch_number","branch_capacity","branch_number_of_tables","branch_google_map_link","branch_country","branch_state","branch_city")
    raw_id_fields = ("branch_city","branch_state","branch_country",'branch_manager')
    list_editable = ('is_translated_content',"is_active",)
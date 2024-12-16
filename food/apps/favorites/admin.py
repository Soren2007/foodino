# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("food","favorite_user","register_date")
    list_filter = ("food","favorite_user","register_date")
    search_fields = ("food","favorite_user","register_date")
    raw_id_fields = ("food","favorite_user")
@admin.register(Favorite_Blog)
class Favorite_BlogAdmin(admin.ModelAdmin):
    list_display = ("blog","favorite_user","register_date")
    list_filter = ("blog","favorite_user","register_date")
    search_fields = ("blog","favorite_user","register_date")
    raw_id_fields = ("blog","favorite_user")
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("food","recipes","blog","commenting_user","comment_text",'is_translated_content',"is_active")
    list_filter = ("food","recipes","blog","commenting_user","is_active")
    search_fields = ("food","recipes","blog","commenting_user","comment_text","is_active")
    raw_id_fields = ("food","recipes","blog","commenting_user","approving_user","comment_parent")
    ordering = ("is_active",)
    list_editable = ('is_translated_content',"is_active",)
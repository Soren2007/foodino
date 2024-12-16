# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Message)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name","family","subject","register_date",'is_translated_content',"is_seen")
    list_filter = ("name","family","subject","register_date","is_seen")
    search_fields = ("name","family","subject","register_date","is_seen")
    list_editable = ('is_translated_content',"is_seen",)
    ordering = ("is_seen",)
@admin.register(UserChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("full_name","phone_number",'is_translated_content',)
    list_filter = ("full_name","phone_number")
    search_fields = ("full_name","phone_number")
    list_editable = ('is_translated_content',)
@admin.register(ChatRoom) 
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("sender_user","receiver_user","message_text","register_date",'is_translated_content')
    list_filter = ("sender_user","receiver_user","message_text","register_date")
    search_fields = ("sender_user","receiver_user","message_text","register_date")
    list_editable = ('is_translated_content',)
    raw_id_fields = ("sender_user","receiver_user","message_parent")
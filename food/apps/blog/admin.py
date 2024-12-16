# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(KeyWord)
class KeyWordAdmin(admin.ModelAdmin):
    list_display = ("word",'is_translated_content',)
    list_filter = ("word",)
    search_fields = ("word",)
    list_editable = ('is_translated_content',)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_article","article_title","article_slug","article_visits","article_publish_date","article_update_date",'is_translated_content',"article_is_active")
    list_filter = ("article_title","article_slug","article_visits","article_publish_date","article_update_date","article_is_active")
    search_fields = ("article_title","article_slug","article_visits","article_publish_date","article_update_date","article_is_active")
    filter_horizontal=('article_key_words','article_author')
    ordering = ("article_is_active",)
    list_editable = ("article_is_active",)
    readonly_fields = ("show_short_image_article",)
    list_editable = ('is_translated_content',)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_author_avatar","author_name","author_family","author_email","author_phone",'is_translated_content',"author_is_active")
    list_filter = ("author_name","author_family","author_email","author_phone","author_is_active")
    search_fields = ("author_name","author_family","author_email","author_phone","author_is_active")
    list_editable = ("author_is_active",)
    readonly_fields = ("show_short_image_author_avatar",)
    list_editable = ('is_translated_content',)
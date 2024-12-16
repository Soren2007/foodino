# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ("group_name",'is_translated_content',)
    list_filter = ("group_name",)
    search_fields = ("group_name",)
    list_editable = ('is_translated_content',)
@admin.register(StuffGroup)
class StuffGroupAdmin(admin.ModelAdmin):
    list_display = ("group_name",'is_translated_content',)
    list_filter = ("group_name",)
    search_fields = ("group_name",)
    list_editable = ('is_translated_content',)
@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_stuff","stuff_name","stuff_price",'is_translated_content',)
    search_fields = ("stuff_name","stuff_price")
    readonly_fields = ("show_short_image_stuff",)
    raw_id_fields = ("stuff_group",)
    list_editable = ('is_translated_content',)
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("meal_name",'is_translated_content',)
    list_filter = ("meal_name",)
    search_fields = ("meal_name",)
    list_editable = ('is_translated_content',)
@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ("recipe_name","recipe_slug","recipe_register_date","recipe_update_date",'is_translated_content',"recipe_is_active")
    list_filter = ("recipe_name","recipe_slug")
    search_fields = ("recipe_name","recipe_slug")
    filter_horizontal = ('recipe_stuffs','recipe_key_words')
    ordering = ("recipe_is_active",)
    list_editable = ('is_translated_content',"recipe_is_active",)
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("show_short_image_food","food_name","food_price","food_time","food_wight","food_calories","food_group",'is_translated_content',"food_is_active")
    list_filter = ("food_name","food_price","food_time","food_wight","food_calories","food_group","food_is_active")
    search_fields = ("food_name","food_price","food_time","food_wight","food_calories","food_group","food_is_active")
    ordering = ("food_is_active",)
    list_editable = ('is_translated_content',"food_is_active",)
    raw_id_fields = ("food_recipes","food_group")
    readonly_fields = ("show_short_image_food",)
@admin.register(FoodStuffType)
class FoodStuffTypeAdmin(admin.ModelAdmin):
    list_display = ("type_name",'is_translated_content',)
    search_fields = ("type_name",)
    filter_horizontal = ('stuffs',)
    list_editable = ('is_translated_content',)
@admin.register(MyRecipes)
class MyRecipesAdmin(admin.ModelAdmin):
    list_display = ("recipes_user","recipes_name","recipes_food",'is_translated_content')
    list_filter = ("recipes_user","recipes_name","recipes_food")
    search_fields = ("recipes_user","recipes_name","recipes_food")
    filter_horizontal = ('recipes_stuffs',)
    raw_id_fields = ("recipes_user","recipes_food")
    list_editable = ('is_translated_content',)
    
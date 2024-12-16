from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Food,FoodGroup,Recipes,Stuff,StuffGroup,Meal,FoodStuffType,MyRecipes
from apps.language.models import Language
from os.path import isfile
from utils import ImageProcessing,Translator_Language,text_sorting
from os import remove



@receiver(post_save,sender=StuffGroup)
def translation_of_texts_from_stuff_group_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        group_name = str(kwargs['instance'].group_name)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(group_name))
        stuff_group_object = StuffGroup.objects.get(id=id)
        stuff_group_object.is_translated_content = True 
        stuff_group_object.save()

@receiver(post_save,sender=FoodGroup)
def translation_of_texts_from_food_group_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        group_name = str(kwargs['instance'].group_name)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(group_name))
        food_group_object = StuffGroup.objects.get(id=id)
        food_group_object.is_translated_content = True 
        food_group_object.save()

@receiver(post_delete,sender=FoodGroup)
def delete_image_from_food_group_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].group_image)
    if isfile(path):
        remove(path)

@receiver(post_save,sender=Stuff)
def translation_of_texts_from_stuff_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        stuff_name = str(kwargs['instance'].stuff_name)
        stuff_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(stuff_name))
        stuff_group_object = Stuff.objects.get(id=stuff_id)
        stuff_group_object.is_translated_content = True 
        stuff_group_object.save()

@receiver(post_delete,sender=Stuff)
def delete_image_from_stuff_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].stuff_image)
    if isfile(path):
        remove(path)

@receiver(post_save,sender=Meal)
def translation_of_texts_from_meal_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        meal_name = str(kwargs['instance'].meal_name)
        meal_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(meal_name))
        meal_object = Meal.objects.get(id=meal_id)
        meal_object.is_translated_content = True 
        meal_object.save()

@receiver(post_save,sender=Recipes)
def translation_of_texts_from_recipes_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        recipe_name = str(kwargs['instance'].recipe_name)
        recipe = str(kwargs['instance'].recipe)
        recipe_summary_text = str(kwargs['instance'].recipe_summary_text)
        recipe_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(recipe_name))
            translator.add_data_po_file(text_sorting(recipe))
            translator.add_data_po_file(text_sorting(recipe_summary_text))
        recipe_object = Recipes.objects.get(id=recipe_id)
        recipe_object.is_translated_content = True 
        recipe_object.save()

@receiver(post_delete,sender=Recipes)
def delete_image_and_files_from_recipe_model(sender, **kwargs):
    image_path = settings.MEDIA_ROOT+str(kwargs['instance'].recipe_image)
    file_path = settings.MEDIA_ROOT+str(kwargs['instance'].recipe_video)
    if isfile(image_path):
        remove(image_path)
    if isfile(file_path):
        remove(file_path)

@receiver(post_save,sender=FoodStuffType)
def translation_of_texts_from_food_stuff_type_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        type_name = str(kwargs['instance'].type_name)
        type_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(type_name))
        food_stuff_type_object = FoodStuffType.objects.get(id=type_id)
        food_stuff_type_object.is_translated_content = True 
        food_stuff_type_object.save()

@receiver(post_save,sender=Food)
def translation_of_texts_from_food_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        food_name = str(kwargs['instance'].food_name)
        food_description = str(kwargs['instance'].food_description)
        food_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(food_name))
            translator.add_data_po_file(text_sorting(food_description))
        food_object = Food.objects.get(id=food_id)
        food_object.is_translated_content = True 
        food_object.save()
    print("saved food -------------------------------------------------------------------")
    path = settings.MEDIA_ROOT+str(kwargs['instance'].food_image)
    if isfile(path):
        image = ImageProcessing(path)
        image.compress_image("webp")
        
@receiver(post_delete,sender=Food)
def delete_image_from_food_model(sender, **kwargs):
    print("deleted food -------------------------------------------------------------------")
    path = settings.MEDIA_ROOT+str(kwargs['instance'].food_image)
    if isfile(path):
        remove(path)

@receiver(post_save,sender=MyRecipes)
def translation_of_texts_from_my_recipes_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        recipes_name = str(kwargs['instance'].recipes_name)
        recipe_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(recipes_name))
        my_recipe_object = Food.objects.get(id=recipe_id)
        my_recipe_object.is_translated_content = True 
        my_recipe_object.save()
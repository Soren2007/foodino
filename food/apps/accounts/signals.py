from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Country,CustomUser,Customer,State,City
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove



@receiver(post_save,sender=State)
def translation_of_texts_from_state_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        name = str(kwargs['instance'].name)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(name)
        state_object = State.objects.get(id=id)
        state_object.is_translated_content = True 
        state_object.save()

@receiver(post_save,sender=City)
def translation_of_texts_from_city_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        name = str(kwargs['instance'].name)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(name)
        city_object = City.objects.get(id=id)
        city_object.is_translated_content = True 
        city_object.save()
        
@receiver(post_save,sender=Country)
def translation_of_texts_from_country_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        name = str(kwargs['instance'].name)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(name)
        country_object = Country.objects.get(id=id)
        country_object.is_translated_content = True 
        country_object.save()

@receiver(post_delete,sender=Country)
def delete_image_from_country_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].photo_of_the_flag)
    if isfile(path):
        remove(path)

        
@receiver(post_save,sender=CustomUser)
def translation_of_texts_from_custom_user_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        name = str(kwargs['instance'].name)
        family = str(kwargs['instance'].family)
        address = str(kwargs['instance'].address)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(name)
            translator.add_data_po_file(family)
            translator.add_data_po_file(text_sorting(address))
        customUser_object = CustomUser.objects.get(id=id)
        customUser_object.is_translated_content = True 
        customUser_object.save()
        
@receiver(post_delete,sender=CustomUser)
def delete_image_from_customUser_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].profile)
    if isfile(path):
        remove(path)
        
@receiver(post_delete,sender=Customer)
def delete_image_from_customer_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].image)
    if isfile(path):
        remove(path)

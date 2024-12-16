from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Gift,Lottery,wheel_of_luck
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=Gift)
def translation_of_texts_from_gift_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        title = str(kwargs['instance'].title)
        description = str(kwargs['instance'].description)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(title))
            translator.add_data_po_file(text_sorting(description))
        gift_object = Gift.objects.get(id=id)
        gift_object.is_translated_content = True 
        gift_object.save()

@receiver(post_save,sender=Lottery)
def translation_of_texts_from_lottery_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        title = str(kwargs['instance'].title)
        description = str(kwargs['instance'].description)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(title))
            translator.add_data_po_file(text_sorting(description))
        lottery_object = Lottery.objects.get(id=id)
        lottery_object.is_translated_content = True 
        lottery_object.save()
        
@receiver(post_delete,sender=Lottery)
def delete_image_from_lottery_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].image)
    if isfile(path):
        remove(path)
        
@receiver(post_save,sender=wheel_of_luck)
def translation_of_texts_from_wheel_of_luck_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        title = str(kwargs['instance'].title)
        description = str(kwargs['instance'].description)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(title))
            translator.add_data_po_file(text_sorting(description))
        wheel_of_luck_object = wheel_of_luck.objects.get(id=id)
        wheel_of_luck_object.is_translated_content = True 
        wheel_of_luck_object.save()
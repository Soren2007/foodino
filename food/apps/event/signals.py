from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Event,Footer_Event,Top_Menu_Event
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove


@receiver(post_save,sender=Event)
def translation_of_texts_from_event_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        event_title = str(kwargs['instance'].event_title)
        event_text = str(kwargs['instance'].event_text)
        event_action_text = str(kwargs['instance'].event_action_text)
        event_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(event_title))
            translator.add_data_po_file(text_sorting(event_text))
            translator.add_data_po_file(text_sorting(event_action_text))
        event_object = Event.objects.get(id=event_id)
        event_object.is_translated_content = True 
        event_object.save()
@receiver(post_delete,sender=Event)
def delete_image_from_event_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].event_image)
    if isfile(path):
        remove(path)
        remove(path)

@receiver(post_save,sender=Footer_Event)
def translation_of_texts_from_footer_event_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        event_title = str(kwargs['instance'].event_title)
        event_action_text = str(kwargs['instance'].event_action_text)
        event_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(event_title))
            translator.add_data_po_file(text_sorting(event_action_text))
        event_object = Footer_Event.objects.get(id=event_id)
        event_object.is_translated_content = True 
        event_object.save()

@receiver(post_save,sender=Top_Menu_Event)
def translation_of_texts_from_top_menu_event_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        event_title = str(kwargs['instance'].event_title)
        event_action_text = str(kwargs['instance'].event_action_text)
        event_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(event_title))
            translator.add_data_po_file(text_sorting(event_action_text))
        event_object = Top_Menu_Event.objects.get(id=event_id)
        event_object.is_translated_content = True 
        event_object.save()
        
@receiver(post_delete,sender=Top_Menu_Event)
def delete_image_from_top_menu_event_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].event_image)
    if isfile(path):
        remove(path) 
        remove(path)
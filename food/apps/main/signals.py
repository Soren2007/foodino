from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Slid,frequently_asked_question
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=Slid)
def translation_of_texts_from_slid_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        slid_title = str(kwargs['instance'].slid_title)
        slid_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(slid_title))
        slid_object = Slid.objects.get(id=slid_id)
        slid_object.is_translated_content = True 
        slid_object.save()

@receiver(post_save,sender=frequently_asked_question)
def translation_of_texts_from_slid_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        question = str(kwargs['instance'].question)
        response = str(kwargs['instance'].response)
        slid_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(question))
            translator.add_data_po_file(text_sorting(response))
        frequently_asked_question_object = frequently_asked_question.objects.get(id=slid_id)
        frequently_asked_question_object.is_translated_content = True 
        frequently_asked_question_object.save()

@receiver(post_delete,sender=Slid)
def delete_image_from_slid_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].slid_image)
    if isfile(path):
        remove(path)
         
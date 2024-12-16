from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Mukbang
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=Mukbang)
def translation_of_texts_from_mukbang_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        description = str(kwargs['instance'].description)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(description))
        mukbang_object = Mukbang.objects.get(id=id)
        mukbang_object.is_translated_content = True 
        mukbang_object.save()

@receiver(post_delete,sender=Mukbang)
def delete_image_and_files_from_mukbang_model(sender, **kwargs):
    image_path = settings.MEDIA_ROOT+str(kwargs['instance'].poster_image)
    file_path = settings.MEDIA_ROOT+str(kwargs['instance'].video)
    if isfile(image_path):
        remove(image_path)
    if isfile(file_path):
        remove(file_path)
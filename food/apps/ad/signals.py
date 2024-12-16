from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Ad
from apps.language.models import Language
from utils import Translator_Language
from os.path import isfile
from os import remove

@receiver(post_save,sender=Ad)
def translation_of_texts_from_ad_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        ad_title = str(kwargs['instance'].ad_title)
        ad_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(ad_title)
        ad_object = Ad.objects.get(id=ad_id)
        ad_object.is_translated_content = True 
        ad_object.save()
@receiver(post_delete,sender=Ad)
def delete_image_from_ad_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].ad_image)
    if isfile(path):
        remove(path) 

from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Delivery,VehicleType
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=VehicleType)
def translation_of_texts_from_vehicle_type_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        vehicle_type = str(kwargs['instance'].vehicle_type)
        vehicle_type_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(vehicle_type))
        vehicle_type_object = VehicleType.objects.get(id=vehicle_type_id)
        vehicle_type_object.is_translated_content = True 
        vehicle_type_object.save()

@receiver(post_delete,sender=Delivery)
def delete_image_from_delivery_model(sender, **kwargs):
    path = settings.MEDIA_ROOT+str(kwargs['instance'].ID_card_image)
    if isfile(path):
        remove(path)
         
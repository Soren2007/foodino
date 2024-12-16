from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Currency,Payment
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=Currency)
def translation_of_texts_from_currency_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        currency = str(kwargs['instance'].currency)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(currency))
        currency_object = Currency.objects.get(id=id)
        currency_object.is_translated_content = True 
        currency_object.save()
        
@receiver(post_save,sender=Payment)
def translation_of_texts_from_payment_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        description = str(kwargs['instance'].description)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(description))
        payment_object = Payment.objects.get(id=id)
        payment_object.is_translated_content = True 
        payment_object.save()
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Promise,Subscription
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=Promise)
def translation_of_texts_from_promise_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        description = str(kwargs['instance'].description)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(description))
        promise_object = Promise.objects.get(id=id)
        promise_object.is_translated_content = True 
        promise_object.save()

@receiver(post_save,sender=Subscription)
def translation_of_texts_from_subscription_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        subscription_title = str(kwargs['instance'].subscription_title)
        subscription_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(subscription_title))
        payment_object = Subscription.objects.get(id=subscription_id)
        payment_object.is_translated_content = True 
        payment_object.save()
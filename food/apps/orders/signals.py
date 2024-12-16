from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.conf import settings
from .models import PaymentType,Order
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=PaymentType)
def translation_of_texts_from_payment_type_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        payment_title = str(kwargs['instance'].payment_title)
        payment_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(payment_title))
        payment_type_object = PaymentType.objects.get(id=payment_id)
        payment_type_object.is_translated_content = True 
        payment_type_object.save()

# @receiver(post_save,sender=Order)
# def translation_of_texts_from_order_model(sender, **kwargs):
#     is_translated_content = kwargs['instance'].is_translated_content
#     if is_translated_content == False:
#         description = str(kwargs['instance'].description)
#         order_id = str(kwargs['instance'].id)
#         for language in Language.objects.filter(language_is_active = True):
#             translator = Translator_Language(language.language_code)
#             translator.add_data_po_file(text_sorting(description))
#         order_object = Order.objects.get(id=order_id)
#         order_object.is_translated_content = True 
#         order_object.save()
    
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DiscountBasket
from apps.language.models import Language
from utils import Translator_Language,text_sorting

@receiver(post_save,sender=DiscountBasket)
def translation_of_texts_from_discount_basket_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        discount_basket = str(kwargs['instance'].discount_basket)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(discount_basket))
            discount_basket_object = DiscountBasket.objects.get(id=id)
            discount_basket_object.is_translated_content = True 
            discount_basket_object.save()
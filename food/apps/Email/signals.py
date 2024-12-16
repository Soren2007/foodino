from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Email
from apps.language.models import Language
from utils import Translator_Language,text_sorting

@receiver(post_save,sender=Email)
def translation_of_texts_from_email_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        message = str(kwargs['instance'].message)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(message))
        email_object = Email.objects.get(id=id)
        email_object.is_translated_content = True 
        email_object.save()
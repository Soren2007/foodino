from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ChatGPT
from apps.language.models import Language
from utils import Translator_Language,text_sorting

@receiver(post_save,sender=ChatGPT)
def translation_of_texts_from_chat_GPT_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        message = str(kwargs['instance'].message)
        answer = str(kwargs['instance'].answer)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(message))
            translator.add_data_po_file(text_sorting(answer))
        chat_gpt_object = ChatGPT.objects.get(id=id)
        chat_gpt_object.is_translated_content = True
        chat_gpt_object.save()
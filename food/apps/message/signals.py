from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Message,UserChatRoom,ChatRoom
from apps.language.models import Language
from utils import Translator_Language,text_sorting
from os.path import isfile
from os import remove

@receiver(post_save,sender=Message)
def translation_of_texts_from_message_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        name = str(kwargs['instance'].name)
        family = str(kwargs['instance'].family)
        message = str(kwargs['instance'].message)
        subject = str(kwargs['instance'].subject)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(name))
            translator.add_data_po_file(text_sorting(family))
            translator.add_data_po_file(text_sorting(message))
            translator.add_data_po_file(text_sorting(subject))
        message_object = Message.objects.get(id=id)
        message_object.is_translated_content = True 
        message_object.save()

@receiver(post_save,sender=UserChatRoom)
def translation_of_texts_from_user_chat_room_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        full_name = str(kwargs['instance'].full_name)
        id = str(kwargs['instance'].full_name)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(full_name))
        user_chat_room_object = UserChatRoom.objects.get(id=id)
        user_chat_room_object.is_translated_content = True 
        user_chat_room_object.save()

@receiver(post_save,sender=ChatRoom)
def translation_of_texts_from_chat_room_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        message_text = str(kwargs['instance'].message_text)
        id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(message_text))
        chat_room_object = ChatRoom.objects.get(id=id)
        chat_room_object.is_translated_content = True 
        chat_room_object.save()

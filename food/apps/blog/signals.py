from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Article,Author,KeyWord
from apps.language.models import Language
from os.path import isfile
from os import remove
from utils import Translator_Language,text_sorting

@receiver(post_save,sender=KeyWord)
def translation_of_texts_from_key_word_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        word = str(kwargs['instance'].word)
        key_word_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(word)
        key_word_object = KeyWord.objects.get(id=key_word_id)
        key_word_object.is_translated_content = True 
        key_word_object.save()

@receiver(post_save,sender=Author)
def translation_of_texts_from_author_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        author_name = str(kwargs['instance'].author_name)
        author_family = str(kwargs['instance'].author_family)
        author_fullname = str(kwargs['instance'].author_fullname)
        author_info = str(kwargs['instance'].author_info)
        author_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(author_name)
            translator.add_data_po_file(author_family)
            translator.add_data_po_file(author_fullname)
            translator.add_data_po_file(text_sorting(author_info))
        author_object = Author.objects.get(id=author_id)
        author_object.is_translated_content = True 
        author_object.save()

@receiver(post_delete,sender=Author)
def delete_image_files_from_author_model(sender, **kwargs):
    image_path = settings.MEDIA_ROOT+str(kwargs['instance'].author_avatar)
    file_path = settings.MEDIA_ROOT+str(kwargs['instance'].author_cv)
    if isfile(image_path):
        remove(image_path)
        
    if isfile(file_path):
        remove(file_path)

@receiver(post_save,sender=Article)
def translation_of_texts_from_author_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        article_title = str(kwargs['instance'].article_title)
        article_summary_text = str(kwargs['instance'].article_summary_text)
        article_main_text = str(kwargs['instance'].article_main_text)
        article_group = str(kwargs['instance'].article_group)
        article_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(article_title)
            translator.add_data_po_file(text_sorting(article_summary_text))
            translator.add_data_po_file(text_sorting(article_main_text))
            translator.add_data_po_file(text_sorting(article_group))
            translator.add_data_po_file(text_sorting(article_group))
        article_object = Article.objects.get(id=article_id)
        article_object.is_translated_content = True 
        article_object.save()
        

@receiver(post_delete,sender=Article)
def delete_image_and_files_from_article_model(sender, **kwargs):
    image_path = settings.MEDIA_ROOT+str(kwargs['instance'].article_main_image)
    file_path = settings.MEDIA_ROOT+str(kwargs['instance'].article_file)
    if isfile(image_path):
        remove(image_path)
        
    if isfile(file_path):
        remove(file_path)

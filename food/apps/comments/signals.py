from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from apps.language.models import Language
from utils import Translator_Language,text_sorting

@receiver(post_save,sender=Comment)
def translation_of_texts_from_comment_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        comment_text = str(kwargs['instance'].comment_text)
        comment_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(text_sorting(comment_text))
        comment_object = Comment.objects.get(id=comment_id)
        comment_object.is_translated_content = True 
        comment_object.save()
        
            
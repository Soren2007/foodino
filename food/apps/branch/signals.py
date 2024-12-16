from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Branch
from apps.language.models import Language
from utils import Translator_Language,text_sorting

@receiver(post_save,sender=Branch)
def translation_of_texts_from_branch_model(sender, **kwargs):
    is_translated_content = kwargs['instance'].is_translated_content
    if is_translated_content == False:
        branch_name = str(kwargs['instance'].branch_name)
        branch_address = str(kwargs['instance'].branch_address)
        branch_id = str(kwargs['instance'].id)
        for language in Language.objects.filter(language_is_active = True):
            translator = Translator_Language(language.language_code)
            translator.add_data_po_file(branch_name)
            translator.add_data_po_file(text_sorting(branch_address))
        branch_object = Branch.objects.get(id=branch_id)
        branch_object.is_translated_content = True 
        branch_object.save()
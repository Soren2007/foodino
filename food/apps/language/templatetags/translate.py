from django import template
# from apps.data_manager.views import create_message_of_language
from django.utils.translation import get_language, activate,gettext, gettext_lazy
from apps.language.models import Language,LanguageFont
register = template.Library()
@register.filter
def translate(value):
    if value != "" or value != None:
        language_code = get_language()
        if language_code != 'fa':
            activate(language_code)
            return gettext(value)
        return value

@register.filter
def set_lang(value):
    return get_language()

@register.filter   
def set_dir(value):
    language_code = get_language()
    try:
        return Language.objects.get(language_code=language_code).language_directionality
    except:
        return value
@register.filter
def set_stylesheet(value):
    return f"css/style_{set_dir(value)}.css"

@register.filter
def set_stylesheet_font(value):
    language_code = get_language()
    return f"css/fonts/{language_code}.css"
 
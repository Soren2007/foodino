# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,redirect
from .models import Language,LanguageFont
from os import mkdir,chdir,listdir
from os.path import exists
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from subprocess import getoutput
from json import dumps
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
def create_language_folder_and_files(request):
    base_path = settings.LOCALE_PATHS[0]
    chdir(base_path)
    for language in Language.objects.all():
        if not exists(f'{base_path}/{language.language_code}'):
            mkdir(f"{language.language_code}")
    chdir(settings.BASE_DIR)
    print(getoutput('python manage.py makemessages --all'))
    return redirect("main_app:index")
def get_all_language():
    language_list = []
    for language in Language.objects.all():
        language_list.append({'language_code':language.language_code,'language_name':language.language_name,})
    str_objects = dumps(language_list,indent=4)
    with open(f'{settings.LOCALE_PATHS[0]}\\information.json','w+') as language_info_json_file:
        language_info_json_file.write(str_objects)
# get_all_language()

from django.utils.translation import to_language
def set_language_with_ip(request):
    to_language(request.GET.get(''))
    


def get_language_code(request):
    from django.utils.translation import get_language
    return {'language_code':get_language()}

# from os.path import exists
# def create_or_update_css_fonts(request):
#     for language_font in LanguageFont.filter(is_active=True):
#         css_string="@font-face {font-family:" + language_font.font_name + ";src:url('" + language_font.font_embedded_opentype_format + ") format('embeddad-opentype'),url('" + language_font.font_truetype_format + "') format('truetype'),url('" + language_font.font_woff_format + "') format('woff'),url('" + language_font.font_woff_2_format + "') format('woff2')}"
#         css_font_file_path = f'{settings.BASE_DIR}/static/css/fonts/{language_font.language.language_code}/{language_font.font_name}.css'
#         if not exists(css_font_file_path):
#             with open(css_font_file_path,'w') as font_css_file:
#                 font_css_file.write(css_string)
#         else:
#             with open(css_font_file_path,'x') as font_css_file:
#                 font_css_file.write(css_string)
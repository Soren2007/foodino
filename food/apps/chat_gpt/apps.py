# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ChatGptConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.chat_gpt'
    verbose_name = _("مدیریت تبلیغات")

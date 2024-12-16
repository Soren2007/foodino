# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class MukbangConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.mukbang'
    verbose_name = _("مدیریت موکبنگ")
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class FoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.food'
    verbose_name = _("مدیریت غذاها")
    
    def ready(self) -> None:
        from . import signals
        return super().ready()
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class GiftConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.gift'
    verbose_name = _("مدیریت هدایا")
    def ready(self) -> None:
        from . import signals
        return super().ready()
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ad'
    verbose_name = _("مدیریت تبلیغات")
    def ready(self) -> None:
        from . import signals
        return super().ready()
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class EmailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Email'
    verbose_name = _("مدیریت ایمیل")
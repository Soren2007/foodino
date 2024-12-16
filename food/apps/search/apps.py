# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.search'

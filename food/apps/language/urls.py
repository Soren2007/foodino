# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='language_app'
urlpatterns = [
    # path('create-language-folder-and-files', create_language_folder_and_files,name='create_language_folder_and_files'),
]
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name = "my_environment_app"
urlpatterns = [
    path('', index,name="my_environment_index"),
]
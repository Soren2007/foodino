# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name = "what_cook_app"
urlpatterns = [
    path('', index ,name="index"),
    path('show-recipes/', show_recipes ,name="show_recipes"),
]
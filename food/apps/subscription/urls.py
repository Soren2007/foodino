# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name = "subscription_app"
urlpatterns = [
    path('index/',index ,name="index"),
]
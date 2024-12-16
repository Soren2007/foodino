# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='ad_app'

urlpatterns = [
    path('show-ads-random/', show_ads_random,name='show_ads_random'),
]
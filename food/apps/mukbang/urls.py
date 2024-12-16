# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='mukbang_app'
urlpatterns = [
    path('add-mukbang/',AddMukbangView.as_view(),name="add_mukbang"),
]
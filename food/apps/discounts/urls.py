# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="accounts_app"
urlpatterns = [
    # path('register/',RegisterUserView.as_view(),name='register'),
]
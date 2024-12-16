# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="email_app"
urlpatterns = [ 
    path('send-emails/', send_emails,name="send_emails"),
]
# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='chat_gpt_app'
urlpatterns = [
    path('open-ai-chat-gpt/',open_ai_chat_gpt,name="open_ai_chat_gpt"),
]
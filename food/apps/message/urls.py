# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name = "message_app"
urlpatterns = [
    path('contact-us/', add_message, name='contact_us'),
    path('show-box/', show_box, name='show_box'),
    path('start-chat-online/', add_user_in_chat_room, name='start_online_chat'),
    path('show-messages/', show_messages, name='show_messages'),
    path('refresh-messages/', refresh_messages, name='refresh_messages'),
    
    path('add-message/', add_message_online_chat, name='send_message'),
    path('show-chat/', show_chat_room, name='show_chat'),
    path('clear-chat/', clear_chat, name='clear_chat'),
    path('manage-chat-room/', manage_chat_room, name='manage_chat_room'),
    path('manage-chat-room/show-messages/', show_messages_in_manage_chat_room, name='show_messages_in_manage_chat_room'),
]
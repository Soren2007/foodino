# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="event_app"
urlpatterns = [
    path('show-random-event/', show_random_event,name="show_random_event"),
    path('show-top-menu-event/', show_top_menu_event,name="show_top_menu_event"),
    path('show-footer-event/', show_footer_event,name="show_footer_event"),
]
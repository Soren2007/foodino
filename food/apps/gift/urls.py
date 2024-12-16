# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="gift_app"
urlpatterns = [ 
    path('show-wheel-of-luck/', show_wheel_of_luck,name="show_wheel_of_luck"),
    path('get-gift-in-wheel-of-luck/', get_gift_in_wheel_of_luck,name="get_gift_in_wheel_of_luck"),
    path('show-lotteries/', show_lotteries,name="show_lotteries"),
    path('wins-lottery/', wins_lottery,name="wins_lottery"),
]
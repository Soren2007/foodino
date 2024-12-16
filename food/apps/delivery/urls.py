# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name='delivery_app'
urlpatterns = [
    path('delivery-panel/', delivery_panel,name='delivery_panel'),  
]

# handler404 = 'apps.main.views.http_status_404'
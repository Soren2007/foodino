# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.urls import path
from .views import *
app_name="payments_app"
urlpatterns = [
    path('zarinpal-payment/<int:order_id>/', ZarinpalPaymentView.as_view(),name="zarinpal_payment"),
    path('verify/', ZarinpalPaymentVerifyView.as_view(),name="zarinpal_payment_verify"),
    path('show-verify-message/<str:message>/', show_verify_message,name="show_verify_message"),
]
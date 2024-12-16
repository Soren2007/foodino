from django.shortcuts import render,redirect
from apps.orders.models import Order
from .models import Delivery
from django.contrib.messages import success,error
from django.utils.translation import gettext_lazy as _
# Create your views here.

def delivery_panel(request):
    if request.user.is_authenticated and request.user.is_delivery: 
        user = request.user
        delivery=Delivery.objects.filter(is_active = True,user=user)
        order = Order.objects.filter(delivery=delivery[0].id)
        return render(request, "delivery/delivery_panel.html", {"orders":order})
    else:
        error(request,_("شما مجوز ورود ندارید!","error"))
        return redirect("main_app:index")
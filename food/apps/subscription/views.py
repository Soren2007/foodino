# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render
from apps.accounts.models import CustomUser
from apps.food.models import Food
from .models import Subscription
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.


def index(request):
    subscriptions = Subscription.objects.filter(is_active=True)
    return render(request, "subscription/index.html", {"subscriptions":subscriptions})

def add_subscription(request):
    return render(request,"subscription/add_subscription.html", {"":""})

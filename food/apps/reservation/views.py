# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render
from .models import *
from utils import  QR
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.

def add_reservation(request):
    Reservation.objects.create()
    user = request.user
    if request.method == "POST":
        branch_id=request.POST.get('branch_id')
        food=request.POST.get('food_id')
        request.POST.get('')
        qr_text = f"{user.id}"
        QR(qr_text,"#ff5033",20,"",f"{user.id}-{user.name}","jpg")

    return render(request, "")
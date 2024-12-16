# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render
from .models import Ad
from django.views.decorators.csrf import requires_csrf_token
from random import randint
# Create your views here.


def show_ads_random(request):
    ads = Ad.objects.filter(ad_is_active = True)
    if len(ads) > 0:
        ad = ads[randint(0,len(ads)-1)]
        return render(request, "ads/show_ad.html", {"ad":ad})

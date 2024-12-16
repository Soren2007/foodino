# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from .models import robot_takes_containers
# Create your views here.


def index(request):
    if request.user.is_authenticated: 
        user = request.user
        objects = robot_takes_containers.objects.filter(is_active = True,country_location=user.country) 
        return render(request, "my_environment/index.html",{'robot_takes_containers':objects})
    else:
        return render(request, "my_environment/index.html")
        
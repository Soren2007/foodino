# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.shortcuts import render,HttpResponse
from .models import Event,Top_Menu_Event,Footer_Event
from random import randint
from django.conf import settings
from django.views.decorators.csrf import requires_csrf_token
from datetime import date
# Create your views here.
def show_random_event(request):
    event = Event.objects.filter(event_is_active = True)
    if len(event) > 0:
        event = event[randint(0,len(event)-1)]
        return render(request, "event/partials/show_random_event.html", {"event":event})
    return HttpResponse("")
def show_top_menu_event(request):
    top_menu_events = Top_Menu_Event.objects.filter(event_is_active = True,event_end_date__gt = date.today())
    length = len(top_menu_events)
    if length != 0:
        top_menu_event = top_menu_events[randint(0,length-1)]
        event_end_date = str(top_menu_event.event_end_date)
        return render(request, "event/partials/show_event_on_top_menu.html", {"top_menu_event":top_menu_event,'event_end_date':event_end_date,"base_dir":settings.BASE_DIR})
    return HttpResponse("")
def show_footer_event(request):
    footer_event = Footer_Event.objects.filter(event_is_active = True)
    if len(footer_event) > 0:
        footer_event = footer_event[randint(0,len(footer_event)-1)]
        return render(request, "event/partials/show_footer_event.html", {"footer_event":footer_event})
    return HttpResponse("")
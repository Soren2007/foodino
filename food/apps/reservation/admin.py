# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import Reservation
# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user","reservation_date_time","branch","is_active")
    search_fields = ("user","reservation_date_time","branch","is_active")
    list_editable = ("is_active",)
    
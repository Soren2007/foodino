# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import robot_takes_containers,my_environment
# Register your models here.

@admin.register(robot_takes_containers)
class RobotTakesContainersAdmin(admin.ModelAdmin):
    list_display = ("model","country_location","is_active")
    list_filter = ("model","country_location")
    search_fields = ("model","country_location","state_location","city_location","register_date")
    raw_id_fields = ("country_location","state_location","city_location")
    list_editable = ("is_active",)
@admin.register(my_environment)
class RobotTakesContainersAdmin(admin.ModelAdmin):
    list_display = ("user","points_unit","robot_takes")
    search_fields = ("user","points_unit","robot_takes")
    raw_id_fields = ("robot_takes",)
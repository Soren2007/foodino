# File version
__version__ = "1.1.1"
# File Description
"""
this python file
"""
from django.contrib import admin
from .models import Scoring
# Register your models here.

@admin.register(Scoring)
class ScoringAdmin(admin.ModelAdmin):
    list_display = ("food","scoring_user","register_date","score")
    list_filter = ("food","scoring_user","register_date","score")
    search_fields = ("food","scoring_user","register_date","score")
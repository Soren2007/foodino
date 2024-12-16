from django import template
from apps.orders.models import how_to_use
register = template.Library()

@register.filter
def show_how_to_use(how_to_use_number):
    return how_to_use[int(how_to_use_number)][1]
from datetime import datetime

from django import template

register = template.Library()
@register.simple_tag
def show_current_time() -> str:
    return datetime.now().strftime("%H:%M")
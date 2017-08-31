from django import template
from django.conf import settings
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def silk(name):
    return format_html("""<img src="{}pinax/images/silk/icons/{}.png" />""",
        settings.STATIC_URL,
        name,
    )

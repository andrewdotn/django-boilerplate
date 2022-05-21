from django import template
from django.conf import settings
from django.utils import safestring
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def frontend():
    return mark_safe(
        """
        <script type="module" src="http://localhost:3000/@vite/client"></script>
        <link rel="stylesheet" href="http://localhost:3000/style.scss">
        <script async type="module" src="http://localhost:3000/index.ts"></script>
        """
    )

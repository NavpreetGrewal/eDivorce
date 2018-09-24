import re

from django import template
from datetime import datetime
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def linebreaksli(value):
    "Converts strings with newlines into <li></li>s"
    value = re.sub(r'\r\n|\r|\n', '\n', value.strip())  # normalize newlines
    lines = re.split('\n', value)
    lines = ['<li>%s</li>' % line for line in lines if line and not line.isspace()]
    return mark_safe('\n'.join(lines))


@register.filter
def date_formatter(value):
    """
        Changes date format from dd/mm/yyyy to dd/mmm/yyyy
    """
    d = datetime.strptime(value, '%d/%m/%Y')
    return d.strftime('%d %b %Y')

@register.simple_tag()
def required(field, size=None, trail=''):
    """ Return the required field value or the not-entered span """

    if field.strip():
        return '%s%s' % (field, trail)
    style = ('min-width: %spx' % size) if size is not None else ''
    return format_html('<span class="form-entry not-complete" style="{}"></span>', style)


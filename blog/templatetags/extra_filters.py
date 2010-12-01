# -*- coding: utf-8 -*-

from django import template

register = template.Library()


@register.filter
def tag_size(relative, arg):
    try:
    return int(relative * int(arg))
    except:
        return u""
tag_size.is_safe = True

from django import template
from datetime import datetime

register = template.Library()

@register.inclusion_tag('header.html', takes_context=True)
def show_header(context):
    if context.request.user.is_authenticated:
        is_student = context.request.user.profile.is_student()
        is_tutor = context.request.user.profile.is_tutor()
    else:
        is_student = False
        is_tutor = False
    return {
        'is_student': is_student,
        'is_tutor': is_tutor
    }

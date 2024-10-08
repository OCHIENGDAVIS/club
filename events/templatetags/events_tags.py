from django import template
from datetime import datetime

from django.contrib.auth import get_user_model

User = get_user_model()

register = template.Library()


@register.filter(name='reverse')
def reverse(value):
    return value[::-1]


@register.simple_tag(name='create_date')
def create_date(date_value=datetime.today()):
    return f'This content was created on {date_value.strftime("%A %B %d, %y")}'


@register.inclusion_tag('events/all_users.html')
def all_users():
    users = User.objects.all()
    return {
        'users': users
    }

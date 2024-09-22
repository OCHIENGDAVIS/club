from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Event, Venue


@register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date']


@register(Venue)
class VenueAdmin(admin.ModelAdmin):
    ...

from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Event, Venue


@register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'event_date']
    search_fields = ['event_name', 'event_date']
    list_filter = ['event_date']

    fieldsets = ((
                     'required information', {
                         'description': 'this fields are required for each event',
                         'fields': (('event_name', 'venue'), 'event_date')
                     }),
                 ('Optional information', {
                     'classes': ('collapse',),
                     'fields': ('description', 'manager')
                 })

    )


@register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']

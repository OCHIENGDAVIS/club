import csv

from django.contrib import admin
from django.contrib.admin.decorators import register
from django.http import HttpResponse

from .models import Event, Venue

admin.site.site_header = 'MyClub Administration'
admin.site.site_title = 'MyClub Site Admin'
admin.site.index_title = 'MyClub Site Admin Home'


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="event_export.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'event_date', 'venue', 'description'])
    for record in queryset:
        rec_list = []
        rec_list.append(record.event_name)
        rec_list.append(record.event_date.strftime('%m%d%Y, %H:%M'))
        rec_list.append(record.description)
        writer.writerow(rec_list)
    return response


export_to_csv.short_description = 'export to csv'

export_to_csv.short_description = 'Export selected events to csv file'


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
    actions = [export_to_csv]


class EventInline(admin.StackedInline):
    model = Event
    fields = ('event_name', 'event_date', 'description', 'venue', 'manager')
    extra = 31


@register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_display_links = ('name',)
    # inlines = [EventInline]

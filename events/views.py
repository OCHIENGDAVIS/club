from datetime import date
import calendar
from calendar import HTMLCalendar

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Event, Venue
from .forms import VenueForm


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = f'MyClub Event Calender - {month_name} {year}'
    cal = HTMLCalendar().formatmonth(year, month)
    return render(request, 'events/index.html', {'title': title, 'cal': cal})


def all_events(request):
    events = Event.objects.all()
    return render(request, 'events/list.html', {'events': events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/detail.html', {'event': event})


def add_venue(request, id):
    event = get_object_or_404(Event, id=id)
    form = VenueForm(request.POST or None, instance=event.venue)
    if form.is_valid():
        form.save()
        return redirect(event.get_absolute_url())
    return render(request, 'events/add_venue.html', {'form': form})

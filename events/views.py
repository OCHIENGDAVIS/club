from datetime import date
import calendar
from calendar import HTMLCalendar
import csv
import io

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.core.paginator import Paginator
from django.template import RequestContext, Template
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Event, Venue
from .forms import VenueForm, CommitteeForm


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
    page = request.GET.get('page', 1)
    events = Event.objects.all().order_by('-event_date')
    paginator = Paginator(events, 2)
    events = paginator.get_page(int(page))
    return render(request, 'events/list.html', {'events': events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/detail.html', {'event': event})


@login_required()
def add_venue(request, id):
    event = get_object_or_404(Event, id=id)
    form = VenueForm(request.POST or None, instance=event.venue)
    if form.is_valid():
        form.save()
        return redirect(event.get_absolute_url())
    return render(request, 'events/add_venue.html', {'form': form})


def get_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="bart.txt"'
    lines = [
        'I will not expose the ignorance of the faculty\n',
        'will not conduct my own fire drills\n',
        'I will not prescribe medication\n',
    ]
    response.writelines(lines)
    return response


def gen_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="venues.csv"'
    writer = csv.writer(response)
    venues = Venue.objects.all()
    writer.writerow(['Venue Name', 'Address'])
    for venue in venues:
        writer.writerow([venue.name, venue.address])
    return response


def gen_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica-Oblique', 14)
    lines = [
        'I will not expose the ignorance of the faculty',
        'I will not conduct my own fire drills',
        'I will not prescribe medication'
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='bart.pdf')


def context_demo(request):
    template = Template('{{ user }} <br>  {{ perms }} <br> {{ request }} <br> {{ messages }}')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def custom_context_processor(request):
    return {'name': 'davis', 'something': 'something'}


def committee_formset(request):
    committee_set = formset_factory(CommitteeForm, extra=3)
    if request.method == 'POST':
        formset = committee_set(request.POST)
        if formset.is_valid():
            data = formset.cleaned_data
            # this data is a list of dictionaries each representing one form
            print(data)
            return HttpResponseRedirect(reverse('events:committee'))
    else:
        formset = committee_set()
        return render(request, 'events/committee.html', {'formset': formset})

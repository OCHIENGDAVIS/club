from datetime import date

from django.shortcuts import render
from django.http import HttpResponse


def index(request, year=None, month=None):
    if year is None and month is None:
        t = date.today()
        month = date.strftime(t, '%b')
        year = t.year
        title = f'MyClub Event Calender - {month} {year}'
    else:
        title = f'MyClb Event Calender - {month} {year}'
    return HttpResponse(f'<h1>{title} </h1>')

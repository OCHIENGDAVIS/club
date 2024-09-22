from django.db import models
from django.conf import settings


class ClubUser(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Venue(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Event(models.Model):
    event_name = models.CharField(max_length=120)
    event_date = models.DateTimeField()
    manager = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='event_managing', blank=True)
    description = models.TextField(blank=True)
    venue = models.ForeignKey(Venue, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.event_name

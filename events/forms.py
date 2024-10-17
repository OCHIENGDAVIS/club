from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from .models import Venue, Event

User = get_user_model()


class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name', 'description')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.venue = Venue.objects.last()
        instance.event_date = datetime.now()
        if commit:
            instance.save()
            instance.manager.add(User.objects.get(username__icontains='admin'))
        return instance


class ContactForm(forms.Form):
    email = forms.CharField(max_length=120)
    name = forms.CharField(max_length=120),
    comment = forms.CharField(widget=forms.Textarea)


class CommitteeForm(forms.Form):
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=120)


class SurveyForm1(forms.Form):
    name = forms.CharField(max_length=120)
    email = forms.EmailField()


class SurveyForm2(forms.Form):
    response1 = forms.CharField(label='What is great about our club?', widget=forms.Textarea)
    response2 = forms.CharField(label='What is not so great about our club?', widget=forms.Textarea)

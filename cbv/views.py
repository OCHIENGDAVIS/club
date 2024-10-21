from django.shortcuts import render, reverse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from club.contact import ContactForm

from events.models import Event
from events.forms import EventForm
from comments.forms import CommentForm


class TemplateViewDemo(TemplateView):
    template_name = 'cbv/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'This is some new title'
        return context


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'cbv/index.html'
    context_object_name = 'events'


class EventDetail(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'cbv/detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'cbv/create.html'

    def get_success_url(self):
        success_url = reverse_lazy('cbv:detail', args=[self.object.id])
        return success_url


class EventEditView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'cbv/update.html'

    def get_success_url(self):
        success_url = reverse_lazy('cbv:detail', args=[self.object.id])
        return success_url


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('cbv:list')
    template_name = 'cbv/delete_confirm.html'


class ContactView(FormView):
    template_name = 'cbv/contact.html'
    success_url = reverse_lazy('cbv:list')
    form_class = ContactForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['name'] = 'Ochieng Ogori'
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        data = form.cleaned_data
        print(data)  # you can do what you want with this information now sen vian email
        return super().form_valid(form)

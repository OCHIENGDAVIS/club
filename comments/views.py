from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import CommentForm
from .models import Comment


class CommentCreate(CreateView):
    template_name = 'events/detail.html'
    form_class = CommentForm
    model = Comment
    success_url = reverse_lazy('events:detail')

    def get_success_url(self):
        return reverse_lazy('events:detail', kwargs={'id': self.object.event.id})

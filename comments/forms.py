from django import forms
from django.shortcuts import get_object_or_404
from events.models import Event

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'cols': 30, 'rows': 2}),
        }

    def form_valid(self, form):
        form.instance.event = get_object_or_404(Event, id=self.kwargs['id'])
        form.instance.user = self.request.user
        return super().form_valid(form)

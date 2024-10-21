from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse

from events.models import Event

User = get_user_model()


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user.username} said {self.body[:100]}... about f{self.event.event_name}'

    def get_absolute_url(self):
        return reverse('comments:detail', args=[self.id])

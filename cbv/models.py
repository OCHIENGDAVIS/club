from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

MEMBER_CHOICES = (
    ('j', 'Junior'),
    ('s', 'Adult'),
    ('s', 'Senior')
)


class MyClubSubscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    member_level = models.CharField(max_length=1, choices=MEMBER_CHOICES)

    def __str__(self):
        return self.user.username

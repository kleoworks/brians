from __future__ import unicode_literals

from django.db import models
from ..login_registration.models import User

class Secret(models.Model):

    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='users')

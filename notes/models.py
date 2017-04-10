from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Note(models.Model):
    user = models.ForeignKey('auth.User')
    notes = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

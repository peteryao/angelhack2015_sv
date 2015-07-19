# SYSTEM DEPENDENCIES
from datetime import datetime

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating "created" and "modified" fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Log(TimeStampedModel):
    user = models.ForeignKey(User)
    record = models.CharField(max_length=1024)
    note = models.CharField(max_length=1024, blank=True)

class Tag(TimeStampedModel):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    user_priority = models.IntegerField(default=1)

class FeedbackModel(TimeStampedModel):
    assigned_to = models.ForeignKey(User)
    completed = models.BooleanField(default=False)
    tag = ArrayField(models.CharField(max_length=128), blank=True)
    sentiment = models.DecimalField(default=0, max_digits=11, decimal_places=10)
    message = models.CharField(max_length=10000)
# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# PROJECT DEPENDENCIES

# APP DEPENDENCIES
from angelhack2015_sv.apps.core.models import *

# Create your models here.
class Email(TimeStampedModel):
    sender = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000)

    def __unicode__(self):
        return self.subject

# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator

# PROJECT DEPENDENCIES

# APP DEPENDENCIES
from angelhack2015_sv.apps.core.models import *

# Create your models here.
class Email(FeedbackModel):
    sender = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.subject

class Voice(FeedbackModel):
    voice_message_raw = models.FileField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=32) # validators should be a list
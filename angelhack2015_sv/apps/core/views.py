# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.shortcuts import render, redirect

# PROJECT DEPENDENCIES

# APP DEPENDENCIES
from angelhack2015_sv.apps.core.models import *
from angelhack2015_sv.apps.parse.models import *

# Create your views here.

def index(request):
    context = {}
    context['emailList'] = Email.objects.filter(completed=False)
    return render(request, 'core/index.html', context)

def frequency(request):
    context = {}
    context['emailList'] = Email.objects.filter(completed=False)

    return render(request, 'core/frequency.html', context)

def test(request):
    # ... exit or deal with failure...
    return redirect(index)
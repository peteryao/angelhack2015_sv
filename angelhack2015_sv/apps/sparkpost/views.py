# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# PROJECT DEPENDENCIES
from sparkpost import SparkPost

# APP DEPENDENCIES
from angelhack2015_sv.apps.core.models import *

# Create your views here.
SPARKPOST_API_KEY = '42245348290e3777bb8274f718ce32ded7b7ddd4'
def index(request):
    context = {}

    return render(request, 'core/index.html', context)

def test(request):
    pass
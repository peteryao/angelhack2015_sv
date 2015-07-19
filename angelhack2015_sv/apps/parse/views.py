# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# PROJECT DEPENDENCIES
from iodpython.iodindex import IODClient

# APP DEPENDENCIES
from angelhack2015_sv.apps.core.models import *

# Create your views here.
APIKEY = '084bf7b0-b5ef-4a6a-9f87-fe6ba45d1131'
APIURL = 'http://api.idolondemand.com/'

def index(request):
    context = {}

    return render(request, 'core/index.html', context)

def test(request):
	context = {}
	client = IODClient(APIURL, APIKEY)
	r=client.post('analyzesentiment',{'text':'I like cats'})
	myjson=r.json()
	print myjson
	client.createIndex('myindex')
	index = client.getIndex('myindex')
	return redirect(index)
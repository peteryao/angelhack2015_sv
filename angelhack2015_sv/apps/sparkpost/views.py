# SYSTEM DEPENDENCIES
from datetime import datetime, timedelta, time, date
import json
import simplejson

# DJANGO DEPENDENCIES
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict

# PROJECT DEPENDENCIES
from sparkpost import SparkPost
from rest_framework.renderers import JSONRenderer

# APP DEPENDENCIES
from angelhack2015_sv.apps.core.models import *
from angelhack2015_sv.apps.parse.models import Email
from angelhack2015_sv.apps.sparkpost.serializers import EmailSerializer

# Create your views here.
SPARKPOST_API_KEY = '42245348290e3777bb8274f718ce32ded7b7ddd4'

def index(request):
    context = {}

    return render(request, 'core/index.html', context)

def test(request):
    context = {}
    sp = SparkPost(SPARKPOST_API_KEY)

    # response = sp.transmission.send(
    #     recipients=['peteryao916@gmail.com'],
    #     template='angel-mail-eng',
    # )
    #
    # print response
    print Email.objects.filter(tag__contains=['bug'])
    print Email.objects.filter(tag__contains=['feature'])
    print Email.objects.filter(tag__contains=['fire'])
    return render(request, 'sparkpost/test.html', context)

def tag_internal_email(request, tag_pk):
    context = {}
    tag = Tag.objects.get(pk=tag_pk)
    email_list = Email.objects.filter(tag__contains=[tag.name.lower()])
    email_json = EmailSerializer(email_list, many=True)
    sp = SparkPost(SPARKPOST_API_KEY)
    print JSONRenderer().render(email_json.data)
    response = sp.transmission.send(
            recipients=['peteryao916@gmail.com'],
            template='angel-mail-eng',
            subject='<{}> - Issue'.format(tag.name),
            substitution_data={'email_all':JSONRenderer().render(email_json.data)},
        )

    return redirect(index)

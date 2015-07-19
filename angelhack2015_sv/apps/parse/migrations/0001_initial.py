# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('feedbackmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.FeedbackModel')),
                ('sender', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.feedbackmodel',),
        ),
        migrations.CreateModel(
            name='Voice',
            fields=[
                ('feedbackmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.FeedbackModel')),
                ('voice_message_raw', models.FileField(upload_to=b'')),
                ('phone_number', models.CharField(blank=True, max_length=32, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
            options={
                'abstract': False,
            },
            bases=('core.feedbackmodel',),
        ),
    ]

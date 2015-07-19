from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from angelhack2015_sv.apps.parse.models import Email

class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Email
        fields = ('id', 'sender', 'subject', 'message', 'sentiment', 'created', )

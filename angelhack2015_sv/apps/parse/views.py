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
	analyzesentiment=r.json()
	sentiment = analyzesentiment['aggregate']['sentiment']
	context['sentiment']=analyzesentiment
	hightlight_sentiment = ''

	for word in analyzesentiment[sentiment]:
		hightlight_sentiment += '{},'.format(word['topic'])

	r=client.post('highlighttext',{'text':'I like cats', 'highlight_expression':'{}'.format(hightlight_sentiment), 'start_tag':'<b>', 'end_tag':'</b>', })
	context['highlight']=r.json()['text']

	index = client.getIndex('mailsift')

	doc1={'reference':'doc1','title':'title1','content':'this is my content'}
	doc2={'reference':'doc2','title':'title2','content':'this is another content'}
	doc3={'reference':'doc3','title':'title2','content':'this is another content'}
	doc4={'reference':'doc2','title':'titleNew','content':'this is another content alksdjflkjasdfkljaslkdf'}
	docs = [doc1, doc2, doc3, doc4]
	index.addDocs([doc1, doc2, doc3, doc4])
	for doc in docs:
		index.pushDoc(doc)
	print index.size()
	index.commit()
	print index.size()


	return render(request, 'parse/test.html', context)
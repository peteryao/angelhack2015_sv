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
from angelhack2015_sv.apps.parse.models import *

# Create your views here.
APIKEY = '084bf7b0-b5ef-4a6a-9f87-fe6ba45d1131'
APIURL = 'http://api.idolondemand.com/'

def index(request):
    context = {}

    return render(request, 'core/index.html', context)

def generate_highlight(request, feedback_pk):
	context = {}
	client = IODClient(APIURL, APIKEY)

	feedback_email = Email.objects.get(pk=feedback_pk)

	r=client.post('analyzesentiment',{'text':feedback_email.message})
	analyzesentiment=r.json()
	sentiment = analyzesentiment['aggregate']['sentiment']
	context['sentiment']=analyzesentiment
	feedback_email.sentiment = 50 + 50 * analyzesentiment['aggregate']['score']
	hightlight_sentiment = ''

	for word in analyzesentiment[sentiment]:
		hightlight_sentiment += '{},'.format(word['topic'])

	r=client.post('highlighttext',{'text':feedback_email.message, 'highlight_expression':'{}'.format(hightlight_sentiment), 'start_tag':'<b>', 'end_tag':'</b>', })
	feedback_email.content=r.json()['text']
	feedback_email.priority = feedback_email.sentiment + 40
	feedback_email.save()
	context['test'] = feedback_email

	return render(request, 'parse/test.html', context)

def generate_tags(request, feedback_pk):
	context = {}
	client = IODClient(APIURL, APIKEY)
	feedback_email = Email.objects.get(pk=feedback_pk)

	index = client.getIndex('mailsift')
	r = client.post('findsimilar', {'text':feedback_email.message, 'indexes':'mailsift'})
	similar_feedback = r.json()
	if similar_feedback['documents']

	# doc1={'reference':feedback_email.pk,'title':feedback_email.subject, 'content':feedback_email.message}
	# docs = [doc1]
	# index.addDocs([doc1])
	# for doc in docs:
	# 	index.pushDoc(doc)
	# print index.size()
	# index.commit()
	# print index.size()
	context['test'] = feedback_email
	return render(request, 'parse/test.html', context)

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
		print hightlight_sentiment + " here"

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
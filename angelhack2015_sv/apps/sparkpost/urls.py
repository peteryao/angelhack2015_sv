from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('sparkpost.views',
    url(r'^$', views.index, name='index'),
)
from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('parse.views',
    url(r'^$', views.index, name='parse_index'),
)
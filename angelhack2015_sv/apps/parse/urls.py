from django.conf.urls import patterns, include, url

from . import views

feedback_pk = r'(?P<feedback_pk>\d+)'

urlpatterns = patterns('parse.views',
    url(r'^$', views.index, name='parse_index'),
    url(r'^test/$', views.test, name='parse_test'),
    url(r'^generate_highlight/{}/$'.format(feedback_pk), views.generate_highlight, name='parse_highlight'),
    url(r'^generate_tags/{}/$'.format(feedback_pk), views.generate_tags, name='parse_tags'),

)
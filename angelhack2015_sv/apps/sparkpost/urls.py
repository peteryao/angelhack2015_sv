from django.conf.urls import patterns, include, url

from . import views

tag_pk = r'(?P<tag_pk>\d+)'

urlpatterns = patterns('sparkpost.views',
    url(r'^$', views.index, name='sparkpost_index'),
    url(r'^send_email/{}/$'.format(tag_pk), views.tag_internal_email, name='sparkpost_send_tag'),
    url(r'^test/$', views.test, name='sparkpost_test'),
)
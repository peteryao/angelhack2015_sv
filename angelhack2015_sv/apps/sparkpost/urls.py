from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('sparkpost.views',
    url(r'^$', views.index, name='sparkpost_index'),
    url(r'^test/$', views.test, name='sparkpost_test'),
)
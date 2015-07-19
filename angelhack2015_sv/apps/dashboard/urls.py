from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('dashboard.views',
    url(r'^$', views.index, name='dashboard_index'),
)
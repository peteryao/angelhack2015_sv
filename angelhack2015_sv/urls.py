from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.models import User

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'angelhack2015_sv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('angelhack2015_sv.apps.core.urls')),
    url(r'^', include('angelhack2015_sv.apps.dashboard.urls')),
    url(r'^parse/', include('angelhack2015_sv.apps.parse.urls')),
    url(r'^sparkpost/', include('angelhack2015_sv.apps.sparkpost.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


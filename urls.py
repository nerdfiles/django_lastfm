from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # url(r'^$', 'django_lastfm.views.home', name='home'),
  # url(r'^django_lastfm/', include('django_lastfm.foo.urls')),

  (r'^lastfm/', include('lastfm.urls')),

  url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  url(r'^admin/', include(admin.site.urls)),
)

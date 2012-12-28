from django.conf.urls.defaults import *

'''
  
  @nerdfiles
'''

urlpatterns = patterns('',
  (r'^$', 'lastfm.views.home'),

  # recent
  (r'^__recent/$', 'lastfm.views.recent_tracks'),
  (r'^__recent/(?P<limit>\d+)?/$', 'lastfm.views.recent_tracks'),

  # loved
  (r'^__loved/$', 'lastfm.views.loved_tracks'),
  (r'^__loved/(?P<limit>\d+)?/$', 'lastfm.views.loved_tracks'),
  
  # last.fm friends
  (r'^__friends/$', 'lastfm.views.friends'),
  (r'^__friends/(?P<limit>\d+)?/$', 'lastfm.views.friends'),
)



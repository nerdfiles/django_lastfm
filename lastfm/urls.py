from django.conf.urls.defaults import *

'''
  
  @nerdfiles
'''

urlpatterns = patterns('',
  (r'^$', 'lastfm.views.home'),

  (r'^__latest/$', 'lastfm.views.recent_tracks'),

  (r'^__loved/$', 'lastfm.views.loved_tracks'),
  
  (r'^__friends/$', 'lastfm.views.friends'),
)



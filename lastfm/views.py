# -*- coding: utf-8 -*-

# == IMPORTS ======================================== #

from django.conf import settings
from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django import http
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from django.template import loader, Context
from django.template.context import RequestContext
from django.http import Http404
from django.template import RequestContext
import logging

# django_lastfm essentials
from pprint import pprint
from django.core.cache import cache
import pylast
from settings import API_KEY, API_SECRET, username, password_hash

# defaults

DEFAULT_LIMIT = 5
DEFAULT_TO = 3600


# == VIEWS ======================================== #

def render_response(request, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(request)
  return render_to_response(*args, **kwargs)

def home(request):
  
  return render_response(request, 'home.tmpl')

def recent_tracks(request, limit=5):

  #sanity check on item limit
  if limit is 0:
    limit = None

  #call api through pylast
  network = pylast.LastFMNetwork(
    api_key = API_KEY, 
    api_secret = API_SECRET, 
    username = username, 
    password_hash = password_hash)
  
  #site-wide caching if available
  network.enable_caching()

  #user
  user_data = network.get_user(username)

  #urls
  base_url = "http://www.last.fm"
  pub_user_url = "%s/user/%s" % (base_url, username,)
  pub_friends_url = "%s/friends" % pub_user_url
  pub_library_url = "%s/library" % pub_user_url
  pub_recent_tracks_url = "%s/tracks" % pub_user_url

  #cache (double cached!)
  cached_recent_tracks = cache.get('cached_recent_tracks')
  if cached_recent_tracks:
    return {
      "pub_recent_tracks_url": pub_recent_tracks_url,
      "pub_user_url": pub_user_url,
      "pub_friends_url": pub_friends_url,
      "pub_library_url": pub_library_url,
      "recent_tracks": cached_recent_tracks,
    }

  #get recent track data
  r_tracks = user_data.get_recent_tracks(limit=limit)

  #list for recent tracks (raw)
  recent_tracks = [r.track for r in r_tracks]

  #set cache for next time
  cache.set(
    "cached_recent_tracks",
    recent_tracks,
    DEFAULT_TO
  )

  #load raw
  return render_response(request, 'recent_tracks.jade', { 
    "pub_recent_tracks_url": pub_recent_tracks_url,
    "pub_user_url": pub_user_url,
    "pub_library_url": pub_library_url,
    "pub_friends_url": pub_friends_url,
    "recent_tracks": recent_tracks, })

def loved_tracks(request):
  return render_response(request, 'loved_tracks.tmpl')

'''
def error_404(request):
  return render_response(request, '404.tmpl')

def error_500(request):
  return render_response(request, '500.tmpl')
'''


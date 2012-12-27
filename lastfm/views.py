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

from pprint import pprint
from django.core.cache import cache
import pylast
from settings import API_KEY, API_SECRET, username, password_hash


# == VIEWS ======================================== #

def render_response(request, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(request)
  return render_to_response(*args, **kwargs)

def home(request):
  return render_response(request, 'home.html')

def recent_tracks(request):
  network = pylast.LastFMNetwork(
    api_key = API_KEY, 
    api_secret = API_SECRET, 
    username = username, 
    password_hash = password_hash)
  
  user_data = network.get_user(username)
  r_tracks = user_data.get_recent_tracks(limit=5)
  recent_tracks = [r.track for r in r_tracks]
  pprint(recent_tracks)

  '''
  user_data = network.get_user(username)
  r_tracks = user_data.get_recent_tracks(limit=5)
  recent_tracks = [r.track for r in r_tracks]
  network.enable_caching()

  #cache
  lfm_data = cache.get('lfm_data')
  TIMEOUT = 1800*36 #secs
  if lfm_data:
    return {
      "rt": recent_tracks
    }

  #raw
  lfm_data = recent_tracks

  #set cache for next time
  cache.set(
    "lfm_data",
    lfm_data,
    TIMEOUT
  )

  #load raw
  return {
    'rt': lfm_data,
  }
  '''
  return render_response(request, 'recent_tracks.tmpl')

def loved_tracks(request):
  return render_response(request, 'loved_tracks.tmpl')

'''
def error_404(request):
  return render_response(request, '404.tmpl')

def error_500(request):
  return render_response(request, '500.tmpl')
'''


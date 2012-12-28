
# call jQuery
$ = jQuery

$.fn.extend

  django_lastfm: (options) ->

    #settings

    settings =
      debug: false

    #extend settings

    settings = $.extend settings, options

    # prepare_lastfm
    #
    # http://domain.com/fm/playing/
    # http://domain.com/fm/latest/<limit>/
    # http://domain.com/fm/loved/<limit>/
    # http://domain.com/fm/friends/<limit>/

    prepare_lastfm = (url) ->

      $.ajax  url,
              type: 'GET'
              dataType: 'html'
              error: (jqXHR, textStatus, errorThrown) ->
                $('body').append "AJAX Error: #{textStatus}"
              success: (data, textStatus, jqXHR) ->
                $('body').append "Success: #{data}"

    #logger

    log = (msg) ->

      console?.log msg if settings.debug

    return @each ()->
      log "Wat"



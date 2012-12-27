
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
    # http://domain.com/fm/latest/5/
    # http://domain.com/fm/loved/5/
    # http://domain.com/fm/friends/5/

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



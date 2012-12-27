# @see http://pastebin.com/raw.php?i=XTDKbQvK
# @author http://javascriptisawesome.blogspot.com/

(->
  _waitUntilExists =
    pending_functions: []
    loop_and_call: ->
      return  unless _waitUntilExists.pending_functions.length
      i = 0

      while i < _waitUntilExists.pending_functions.length
        obj = _waitUntilExists.pending_functions[i]
        resolution = document.getElementById(obj.id)
        resolution = document.body  if obj.id is document
        if resolution
          _f = obj.f
          _waitUntilExists.pending_functions.splice i, 1
          obj.c = resolution  if obj.c is "itself"
          _f.call obj.c
          i--
        i++

    global_interval: setInterval(->
      _waitUntilExists.loop_and_call()
    , 5)

  if document.addEventListener
    document.addEventListener "DOMNodeInserted", _waitUntilExists.loop_and_call, false
    clearInterval _waitUntilExists.global_interval
  window.waitUntilExists = (id, the_function, context) ->
    context = context or window
    if typeof id is "function"
      context = the_function
      the_function = id
      id = document
    _waitUntilExists.pending_functions.push
      f: the_function
      id: id
      c: context


  waitUntilExists.stop = (id, f) ->
    i = 0

    while i < _waitUntilExists.pending_functions.length
      _waitUntilExists.pending_functions.splice i, 1  if _waitUntilExists.pending_functions[i].id is id and (typeof f is "undefined" or _waitUntilExists.pending_functions[i].f is f)
      i++

  waitUntilExists.stopAll = ->
    _waitUntilExists.pending_functions = []
)()


#Django Last.FM

##Deps

1. [pylast](https://code.google.com/p/pylast/)
2. [coffeescript](http://coffeescript.org/)
3. [pyjade](https://github.com/SyrusAkbary/pyjade)

##pyjade

See [https://github.com/SyrusAkbary/pyjade](https://github.com/SyrusAkbary/pyjade).

##pylast configuration

Set the following in ``settings.py``:

    username = "USER"
    password_hash = pylast.md5("PASS")
    API_KEY = "APIKEY" 
    API_SECRET = "APISECRET"

##RESTful ideas

* http://domain.com/fm/playing/
* http://domain.com/fm/latest/5/
* http://domain.com/fm/loved/5/
* http://domain.com/fm/friends/5/


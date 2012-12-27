#Django Last.FM

##Deps

1. pylast
2. coffeescript

##pylast

Set the following in ``settings.py``:

    username = "USER"
    password_hash = pylast.md5("PASS")
    API_KEY = "APIKEY" 
    API_SECRET = "APISECRET"

##RESTful ideas

http://domain.com/fm/playing/
http://domain.com/fm/latest/5/
http://domain.com/fm/loved/5/
http://domain.com/fm/friends/5/


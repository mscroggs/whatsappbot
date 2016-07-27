from __future__ import division
from datetime import datetime

def ping(message):
    return "Pong!"

def emf(message):
    delta = datetime(2016,8,5,11) - datetime.now()
    return str(delta.days)+" days, "+str(delta.seconds//3600)+" hours until EMF2016"

def date(message):
    return datetime.now().strftime("%Y-%m-%d %H:%M GMT")

def help(message):
    return "Hi, I'm ScroggsBot. Send me commands starting with a ?. Try: ?ping, ?date, ?emf"

actiondict = {
    "ping":ping,
    "emf":emf,
    "help":help,
    "date":date
   }

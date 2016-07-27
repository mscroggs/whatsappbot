from __future__ import division
from datetime import datetime
from random import choice

def ping(message):
    return "Pong!"

def github(message):
    return "You can find my source code at https://github.com/mscroggs/whatsappbot"

def emf(message):
    delta = datetime(2016,8,5,11) - datetime.now()
    return str(delta.days)+" days, "+str(delta.seconds//3600)+" hours until EMF2016"

def date(message):
    return datetime.now().strftime("%Y-%m-%d %H:%M GMT")

def help(message):
    return "Hi, I'm ScroggsBot. Send me commands starting with a ?. Try: ?"+choice(actiondict)+", ?"+choice(actiondict)+" or ?"+choice(actiondict)+""

def month(message):
    if datetime.now().month == 5:
        return "'Tis the month of Maying!"
    return "'Tis not the month of Maying!"

actiondict = {
    "github":github,
    "git":github,
    "ping":ping,
    "emf":emf,
    "help":help,
    "date":date,
    "month":month
   }

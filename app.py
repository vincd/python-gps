#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0

import os
from gps import *
from time import *
import time
import threading

from flask import Flask
from flask import render_template


app = Flask(__name__)
gpsd = None #seting the global variable
previous_latitude = 0
previous_longitude = 0

def isnan(x): return str(x) == 'nan'

class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


@app.route('/map')
def app_map():
  global previous_latitude, previous_longitude
  infos = ', '.join(map(lambda s: str(s), gpsd.satellites))

  if not isnan(gpsd.fix.latitude):
    previous_latitude = gpsd.fix.latitude

  if not isnan(gpsd.fix.longitude):
    previous_longitude = gpsd.fix.longitude

  return render_template('map.html',
      latitude=previous_latitude,
      longitude=previous_longitude,
      informations=infos)


if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread

  try:
    gpsp.start() # start it up
    app.run(debug=True)

  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."

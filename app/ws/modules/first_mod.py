#!/usr/bin/env python

import datetime
from flask_socketio import emit
import time 

def first_response(socketio, secs, resp_id):
    while True:
        socketio.sleep(secs)
        socketio.emit(
                resp_id, 
                {'data': '{}'.format(datetime.datetime.now())}, 
                namespace='/ws'
        )
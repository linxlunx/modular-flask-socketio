from app import socketio
from app.ws.modules.first_mod import first_response
from app.ws.modules.second_mod import second_response
from flask import Blueprint
from threading import Lock

ws = Blueprint('ws', __name__)

first_thread = None
second_thread = None

thread_lock = Lock()

# function to create background task on connect
def start_background(target, secs, resp_id):
    socket_thread = socketio.start_background_task(
        target=target, 
        socketio=socketio, 
        secs=secs,
        resp_id=resp_id
    )

    return socket_thread

@socketio.on('connect', namespace='/ws')
def ws_connect():
    global first_thread
    global second_thread
    
    with thread_lock:
        if first_thread is None:
            first_thread = start_background(first_response, 3, 'first_response')
        if second_thread is None:
            second_thread = start_background(second_response, 5, 'second_response')
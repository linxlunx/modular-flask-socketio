from flask import Flask, render_template, Blueprint
from flask_socketio import SocketIO, emit
import datetime
import time
from threading import Lock

async_mode = None

app = Flask(__name__)
app.config.from_object('config')

# socketio initialization here
socketio = SocketIO(app, async_mode=async_mode)

# no need to do register blueprint for ws module, but still need to be imported 
from app.ws.controllers import ws
from app.welcome.controllers import welcome

app.register_blueprint(welcome)



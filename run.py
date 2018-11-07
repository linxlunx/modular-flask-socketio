#!/usr/bin/env python

import click
from app import app, socketio
import config

# dynamic ip and port for running the server
@click.command()
@click.option('--ip', '-i', default=config.SERVER_HOST, help='Webservice Host', show_default=True)
@click.option('--port', '-p', default=config.SERVER_PORT, help='Webservice Port', show_default=True)
def run_server(ip, port):
    socketio.run(app, host=ip, port=port)

if __name__ == '__main__':
    run_server()
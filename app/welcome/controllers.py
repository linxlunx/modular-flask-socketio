#!/usr/bin/env python

from flask import Blueprint, request, Response, render_template

welcome = Blueprint('welcome', __name__, url_prefix='/')

@welcome.route('')
def index():
    return render_template('welcome/index.html')
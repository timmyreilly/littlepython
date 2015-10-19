"""
Routes and views for the flask application.
"""

from flask import render_template
from myapplication import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tim'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)
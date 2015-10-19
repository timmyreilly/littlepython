"""
Routes and views for the flask application.
"""

from flask import Flask
from myapplication import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'TIM'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''
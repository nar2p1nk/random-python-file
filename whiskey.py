from flask import Flask
from markupsafe import escape
application = Flask(__name__)

@application.route('/')
def default():
    return 'this is the flask default (created by me)'

@application.route('/34.xxx')
def normal():
    return'<h2>Uwu</h2>'

@application.route('/<name>')
def name(name):
    return f"<h1>hey {escape(name)}</h1>"

@application.route('/<name>/<object>')
def crack(name,object):
    return f"<h2>hey {escape(name)}, you dropped your {escape(object)}</h2>"

@application.route('/34.xxx/<int:id>')
def num(id):
    return f"<h2> the {id}th post</h2>"


# https://rule34.xxx/index.php?page=post&s=view&id=4998257
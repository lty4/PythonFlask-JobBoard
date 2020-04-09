from flask import Flask
from flask import render_template

app = Flask(__name__)


def jobs():
    return render_template('index.html')


def route(url):
    jobs()
    return '/'

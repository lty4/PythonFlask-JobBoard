from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

app = Flask(__name__)


def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection, g._connection = sqlite3.connection(PATH)


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

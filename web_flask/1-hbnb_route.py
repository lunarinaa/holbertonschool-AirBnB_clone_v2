#!/usr/bin/python3
from flask import Flask
"""starting flask web app"""

app = Flask(__name__)
"""object of Flask class"""


@app.route('/', strict_slashes=False)
def display():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_display():
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

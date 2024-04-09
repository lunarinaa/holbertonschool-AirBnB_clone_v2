#!/usr/bin/python3
from flask import Flask 

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display():
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def hbnb_display():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_display(text):
    return f'C {text.replace('_', ' ')}'

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_display(text='is cool'):
    return f'Python {text.replace('_', ' ')}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
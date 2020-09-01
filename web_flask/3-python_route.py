#!/usr/bin/python3
""" starts a Flask web application ss"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ flask """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ flask """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def CisC(text):
    """ flask """
    strs = text.replace("_", " ")
    return ("C %s" % strs)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ispython(text="is cool"):
    """ flask """
    strs = text.replace("_", " ")
    return ("Python %s" % strs)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

#!/usr/bin/python3
""" starts a Flask web application ss"""
from flask import Flask, render_template


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
    """ C is weird """
    strs = text.replace("_", " ")
    return ("C %s" % strs)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ispython(text="is cool"):
    """ python is cool"""
    strs = text.replace("_", " ")
    return ("Python %s" % strs)


@app.route('/number/<int:n>', strict_slashes=False)
def isinteger(n):
    """ flask is an integer """
    return ("%d is a number" % n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def istemplate(n):
    """ flask using a html template"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def isevenorodd(n):
    """ flask even or odd """
    if n % 2 == 0:
        pori = "even"
    else:
        pori = "odd"
    return render_template("6-number_odd_or_even.html", n=n, pori=pori)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

#!/usr/bin/python3
""" starts a Flask web application ss"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def indexairbnb():
    """ print all cities """
    all_states = storage.all(State)
    all_ameninty = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", all_states=all_states,
                           all_ameninty=all_ameninty)


@app.teardown_appcontext
def teardowndb(response_or_exc):
    """ session close """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

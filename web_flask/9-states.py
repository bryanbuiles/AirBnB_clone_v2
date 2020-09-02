#!/usr/bin/python3
""" starts a Flask web application ss"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states/', strict_slashes=False)
def statescomplex():
    """ print all states """
    all_states = storage.all(State)
    return render_template("9-states.html", all_states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def citieshtmlcomplex(id):
    """ print all cities """
    all_states = storage.all(State)
    stateid = 'State.' + id
    return render_template("9-states.html", all_states=all_states,
                           id=id, stateid=stateid)


@app.teardown_appcontext
def teardowndb(response_or_exc):
    """ session close """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')

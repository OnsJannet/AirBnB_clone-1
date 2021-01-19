#!/usr/bin/python3
''' Flask web application '''

from flask import Flask
from flask import render_template
from models.state import State
from models.city import City
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    states = storage.all(State)
    cities = storage.all(City)
    return render_template('8-cities_by_states.html', states=all_states, 
                           cities=all_cities)


@app.teardown_appcontext
def teardown_appcontext(self):
    return storage.close()

#!/usr/bin/python3
''' Flask web application '''

from flask import Flask
from flask import render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state(id=None):
    all_states = storage.all(State)
    all_amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=all_states, 
                           amenities=all_amenities)


@app.teardown_appcontext
def teardown_appcontext(self):
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
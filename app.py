# Import the dependencies.

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

#################################################
# Database Setup
#################################################

# Initialize the Flask application
app = Flask(__name__)

# Set the database URI

# Create a SQLAlchemy instance


# Create an engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = db.session

#################################################
# Flask Setup
#################################################

@app.route('/')
def index():
    return "Welcome to the Climate App!"

#################################################
# Flask Routes
#################################################

@app.route('/measurements')
def get_measurements():
    results = session.query(Measurement).all()
    measurements = []
    for measurement in results:
        measurements.append({
            'date': measurement.date,
            'temperature': measurement.tobs,
            'precipitation': measurement.prcp
        })
    return jsonify(measurements)

@app.route('/stations')
def get_stations():
    results = session.query(Station).all()
    stations = []
    for station in results:
        stations.append({
            'station_id': station.station,
            'station_name': station.name,
            'latitude': station.latitude,
            'longitude': station.longitude
        })
    return jsonify(stations)

if __name__ == '__main__':
    app.run(debug=True)
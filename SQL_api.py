import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

hawaii_path = '/Users/connorturnage/Desktop/hawaii.sqlite'
engine = create_engine(f"sqlite:///{hawaii_path}", echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)
mes = Base.classes.measurement
stat = Base.classes.station


app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")

def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(mes.date, mes.prcp).\
    filter(mes.date >= '2016-08-23').\
    order_by(mes.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)



@app.route("/api/v1.0/stations")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(stat.station).group_by('id')

    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all passengers
    results = session.query(mes.tobs, mes.date).\
    filter(mes.date >= '2016-08-23').\
    group_by(mes.date).\
    order_by(mes.date)

    session.close()

     # Create a dictionary from the row data and append to a list of all_passengers
    all_tobs = []
    for date, tobs in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)
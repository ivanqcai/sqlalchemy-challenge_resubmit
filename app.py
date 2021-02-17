import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station =Base.classes.station

session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():



    """Return a list of all passenger names"""

    results = session.query(Measurement.date,Measurement.prcp).all()

    session.close()

    result_dict={date:pcrp for date,prcp in results}

    return jsonify(result_dict)


@app.route("/api/v1.0/stations")
def stations():


    results = session.query(Station.station).all()

    session.close()

    result_list= list(np.ravel(results))




    return jsonify(result_list)


@app.route("/api/v1.0/tobs")
def stations():

    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""

    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).filter(Measurement.date>=one_year).\
    filter(Measurement.station==)

    session.close()

    result_list= list(np.ravel(results))



    return jsonify(result_list)

@app.route("/api/v1.0/<start>")
def start():

    session = Session(engine)

    results= session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>=start).all()

    result_list= list(np.ravel(results))
    return jsonify(result_list)

@app.route("/api/v1.0/<start>/<end>")
def start():

    session = Session(engine)

    start_end = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date between start,end).all()
    start_end = pd.DataFrame(temperature_observ, columns=['temperature'])


if __name__ == '__main__':
    app.run(debug=True)
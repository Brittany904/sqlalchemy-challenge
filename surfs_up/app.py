# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement

Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)



#################################################
# Flask Routes
#################################################
#homepage route
@app.route("/")
def home():
    """All available routes"""
    
    return (
        f"Welcome to Surfs Up!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"//api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]<br/>"
       
    )
#precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    grab = sesssion.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-24").\
        all()
    
    session.close()

    precipitation = []
    for date, prcp in grab:
        prcp_d = {}
        prcp_d["Date"] = date
        prcp_d["Precipitation"] = prcp
        precipitation.append(precp_d)

    return jsonify(precipitation)

#stations route
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    """All of the Stations"""
    grab = session.query(Station.station).\
                order_by(Station.station).all()
    
    session.close()

    get_stations = list(np.ravel(results))

    return jsonify(get_stations)




#the tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    grab = session.query(Measurement.date, Measurement.tobs, Measurement.prcp).\
                filter(Measurement.date >= "2017-08-23").\
                filter(Measurement.station=='USC00519281').\
                order_by(Measurement.date).all()
                
    session.close()

    tobsact = []
    for date, tobs in grab:
        tobs_d = {}
        tobs_d["Date"] = date
        tobs_d["Tobs"] = tobs
        tobsact.append(tobs_d)

    return jsonify(tobsact)


#start route

#start and end route

if __name__ == "__main__":
    app.run(debug=True)






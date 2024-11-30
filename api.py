import re
from datetime import datetime

import data
from flask import Flask, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from main import SQLITE_URI

# INSTANTIATE DATABASE
DATA_MANAGER = data.FlightData(SQLITE_URI)

# INSTANTIATE FLASK APP
app = Flask(__name__)
app.config["DEFAULT_MIMETYPE"] = "application/json"

# RATE LIMITER
limiter = Limiter(app=app, key_func=get_remote_address)

# SORTING OPTIONS FOR QUERY PARAMETER "sort"
SORT_OPTIONS = ("delay_airline", "delay_airport")


# ROUTES ######################################################################
@app.route("/api/flights", methods=["GET"])
@limiter.limit("30/minute")
def handle_flights():
    # QUERY PARAMETER: "?id=xxxx" -- filter flights by ID
    flight_id = request.args.get("id", None)
    flight_date = request.args.get("date", None)
    airline_delay = request.args.get("airline_delay", None)
    airport_delay = request.args.get("airport_delay", None)

    # PARAMETER CHECK
    if flight_id:
        if id_valid(flight_id):
            output = DATA_MANAGER.get_flight_by_id(flight_id)
        else:
            return jsonify(error="Invalid flight id"), 400

    elif flight_date:
        if date_valid(flight_date):
            day, month, year = get_date(flight_date)
            output = DATA_MANAGER.get_flights_by_date(day, month, year)
        else:
            return jsonify(error="Invalid date"), 400

    elif airline_delay:
        output = DATA_MANAGER.get_delayed_flights_by_airline(airline_delay)

    elif airport_delay:
        output = DATA_MANAGER.get_delayed_flights_by_airport(airport_delay)

    if output:
        # SERIALIZE RESULT TO DICT FOR JSONIFY
        serialized_output = serialize_to_dict(output)

        return jsonify(serialized_output), 200

    return jsonify(error="Nothing found"), 404


# ERROR HANDLING ##############################################################
@app.errorhandler(404)
def not_found_error(error):
    return jsonify(error="Not Found"), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify(error="Method Not Allowed"), 405


@app.errorhandler(429)
def request_error(error):
    return jsonify(error="Too Many Requests"), 429


# HELPER FUNCTIONS ############################################################
def id_valid(flight_id):
    if not flight_id:
        return False
    return flight_id.isdigit() and len(flight_id) <= 7


def date_valid(date):
    if not date:
        return False
    # DATE PATTERN: 03/11/9999 - year is only limited to four digits
    pattern = r"\b(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}\b"

    # Check if the date matches the format
    if not re.fullmatch(pattern, date):
        return False

    day, month, year = get_date(date)

    # CHECK FOR REAL EXISTING DATE
    try:
        date_obj = datetime(year, month, day)

        # CHECK FOR DATE IN FUTURE
        if datetime.now() < date_obj:
            return False

    except ValueError:
        return False

    return True


def get_date(date):
    return map(int, date.split("/"))


def serialize_to_dict(flight_list):
    output = []
    for fi in flight_list:
        flight_dict = {
            "ID": fi[0],
            "YEAR": fi[1],
            "MONTH": fi[2],
            "DAY": fi[3],
            "DAY_OF_WEEK": fi[4],
            "AIRLINE": {"ID": fi[5], "NAME": fi[32]},
            "FLIGHT_NUMBER": fi[6],
            "TAIL_NUMBER": fi[7],
            "ORIGIN_AIRPORT": fi[8],
            "DESTINATION_AIRPORT": fi[9],
            "SCHEDULED_DEPARTURE": fi[10],
            "DEPARTURE_TIME": fi[11],
            "DEPARTURE_DELAY": fi[12],
            "TAXI_OUT": fi[13],
            "WHEELS_OFF": fi[14],
            "SCHEDULED_TIME": fi[15],
            "ELAPSED_TIME": fi[16],
            "AIR_TIME": fi[17],
            "DISTANCE": fi[18],
            "WHEELS_ON": fi[19],
            "TAXI_IN": fi[20],
            "SCHEDULE_ARRIVAL": fi[21],
            "ARRIVAL_TIME": fi[22],
            "ARRIVAL_DELAY": fi[23],
            "DIVERTED": fi[24],
            "CANCELLED": fi[25],
            "CANCELLATION_REASON": fi[26],
            "AIR_SYSTEM_DELAY": fi[27],
            "SECURITY_DELAY": fi[28],
            "AIRLINE_DELAY": fi[29],
            "LATE_AIRCRAFT_DELAY": fi[30],
            "WEATHER_DELAY": fi[31],
        }

        output.append(flight_dict)

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

from operator import is_
from tkinter.tix import Tree
import jinja2 
from jinja2.filters import FILTERS
from flask import Flask, render_template, get_template_attribute, request, jsonify
from helpers import get_time_str, is_active

VERSION = "0.0.1"

app = Flask(__name__)

## SETUP FILTERS AND ENVIROMETNS DATA
FILTERS["is_active"] = is_active

sonar_data ={
    "Latitude": "50.2626",
    "Longituge": "15.545",
    "Altitude": "99.876",
    "Fix-status": "RTK-FIX",
}

## APPLICATION
@app.route("/")
def index():
    return render_template("index.html", version = VERSION, sonar_data = sonar_data,update_time = get_time_str())


@app.route("/get_table_data")
def get_table_data():
    table_data = get_template_attribute("_table_body.html","table_data")
    return table_data(sonar_data)

@app.route("/get_json_data")
def get_json_data():
    return jsonify(sonar_data)

@app.route("/put_data",methods=['POST','GET'])
def put_data():
    global sonar_data
    if request.method == 'POST':
        sonar_data = request.get_json()
        return jsonify(sonar_data)
    else:
        return render_template("about.html", version = VERSION)

@app.route("/about")
def about():
    return render_template("about.html", version = VERSION)

@app.route("/test")
def test():
    return render_template("page_template.html", version = VERSION)


#TODO: automaticky reload stranky
#TODO: upraveni vzhledu radku
#TODO: doplneni about stranky
#TODO: udelat base template a extend z nej

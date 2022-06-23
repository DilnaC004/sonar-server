import os
#import setproctitle

from datetime import datetime
from jinja2.filters import FILTERS
from flask import Flask, render_template, request, jsonify, send_from_directory
from helpers import get_time_str, is_active, SonarData


VERSION = "0.0.1"
# setproctitle.setproctitle("SonarServer")

app = Flask(__name__)

# SETUP FILTERS AND ENVIROMETNS DATA
FILTERS["is_active"] = is_active

sonar_data = SonarData()

# APPLICATION


@app.route("/")
def index():
    return render_template("index.html", version=VERSION, sonar_data=sonar_data.get_data()[0], update_time=get_time_str())


@app.route("/get_table_data")
def get_table_data():
    s_data, time_str = sonar_data.get_data()
    html_str = render_template("table_body.html", sonar_data=s_data)
    return jsonify([html_str, time_str])


@app.route("/get_json_data")
def get_json_data():
    return jsonify(sonar_data.get_data())


@app.route("/send_data", methods=['POST', 'GET'])
def put_data():
    global sonar_data
    if request.method == 'POST':
        sonar_data.set_data(dict(request.get_json()))
        return jsonify(sonar_data.get_data())
    else:
        return render_template("about.html", version=VERSION)


@app.route("/about")
def about():
    return render_template("about.html", version=VERSION)


@app.route("/map")
def map():
    return render_template("map.html", version=VERSION)


@app.route("/settings")
def setting():
    return render_template("settings.html", version=VERSION)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static", "img"),
                               "favicon.ico", mimetype="image/vnd.microsoft.icon")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

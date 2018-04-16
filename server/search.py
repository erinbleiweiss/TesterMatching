from flask import Flask, jsonify, request
from flask_cors import CORS
from collections import OrderedDict

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
CORS(app)

from testerDAO import TesterDAO


@app.route("/", methods=["GET"])
def index():
    return "Tester Matching App"


@app.route("/countries", methods=["GET"])
def get_countries():
    dao = TesterDAO()
    return jsonify(dao.get_countries())


@app.route("/devices", methods=["GET"])
def get_devices():
    dao = TesterDAO()
    return jsonify(dao.get_devices())


@app.route("/search", methods=["GET"])
def search():
    dao = TesterDAO()
    country_params = request.args.get('country').split('|')
    device_params = request.args.get('device').split('|')
    return jsonify(dao.search(country_filter=country_params,
                              device_filter=device_params))

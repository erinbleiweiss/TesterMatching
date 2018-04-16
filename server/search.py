from flask import Flask, jsonify, request
from flask_cors import CORS
from pprint import pprint

app = Flask(__name__)
CORS(app)

from testerDAO import TesterDAO


@app.route("/get_countries", methods=["GET"])
def get_countries():
    dao = TesterDAO()
    return jsonify(dao.get_countries())


@app.route("/get_devices", methods=["GET"])
def get_devices():
    dao = TesterDAO()
    return jsonify(dao.get_devices())


@app.route("/search", methods=["GET"])
def search():
    dao = TesterDAO()
    country_params = request.args.get('country')
    device_params = request.args.get('device')
    return jsonify(dao.search(country_filter=[], device_filter=[]))

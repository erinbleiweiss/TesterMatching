from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from testerDAO import TesterDAO


@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    dao = TesterDAO()
    countries = dao.get_countries()
    devices = dao.get_devices()

    res = dao.search(country_filter=['US'], device_filter=['iPhone 4S', 'Nexus 4'])
    print(res)


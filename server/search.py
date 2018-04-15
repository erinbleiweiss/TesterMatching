from flask import Flask, request
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "Hello World!"


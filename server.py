import os

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from gather import Gather
from flask import request
import json


g = Gather()

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html", json=g.get_json(3,300), json2=g.get_json(2,10))

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory("js", path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory("css", path)

@app.route("/semantic/<path:path>")
def send_semantic(path):
    return send_from_directory("semantic", path)

@app.route("/cluster")
def cluster():
    return json.dumps(g.get_json(int(request.args.get("num")), 10))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

def get_app():
    return app

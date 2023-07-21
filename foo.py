import os

import requests
from flask import Flask
from flask import make_response
from waitress import serve

app = Flask(__name__)


@app.route("/foo", methods=["POST"])
def foo():
    r = requests.post("http://localhost:5000/sidecar", json={})
    return make_response("foo", 200)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

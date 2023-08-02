import logging
import os

import requests
import google.cloud.logging
from flask import Flask
from flask import make_response
from waitress import serve

app = Flask(__name__)
client = google.cloud.logging.Client()
client.setup_logging()

@app.route("/foo", methods=["POST"])
def foo():
    try:
        r = requests.post("http://localhost:5000/sidecar", json={})
    except:
        logging.error("foo is available but sidecar isn't")
        return make_response("bar", 400)
    logging.info("both foo and sidecar are available")
    return make_response("foo", 200)


@app.route("/", methods=["GET"])
def health_check():
    return make_response("ok", 200)



if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

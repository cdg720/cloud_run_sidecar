import logging
import os

import google.cloud.logging
from flask import Flask
from flask import make_response
from flask import request
from waitress import serve

app = Flask(__name__)
client = google.cloud.logging.Client()
client.setup_logging()

from langchain import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents import BaseSingleActionAgent
from langchain.agents import Tool
from langchain.schema import AgentAction
from langchain.schema import AgentFinish


@app.route("/sidecar", methods=["POST"])
def sidecar():
    d = request.get_json()
    logging.info(f"params: {d}")

    return make_response("sidecar", 200)


@app.route("/", methods=["GET"])
def health_check():
    return make_response("ok", 200)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logging.info(f"Starting sidecar service on port {port}")
    serve(app, host="0.0.0.0", port=port)
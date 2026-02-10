import logging
import json
import os
from flask import Flask, jsonify

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)

logger = logging.getLogger()

APP_ENV = os.getenv("APP_ENV", "development")

app = Flask(__name__)

# Startup log
logger.info(json.dumps({
    "event": "app_startup",
    "status": "success",
    "app_env": APP_ENV
}))

@app.route("/")
def home():
    logger.info(json.dumps({
        "event": "request_received",
        "path": "/",
        "method": "GET",
        "app_env": APP_ENV
    }))

    return jsonify({
        "status": "ok",
        "service": "devsecops-demo",
        "environment": APP_ENV
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = "/data/visits.txt"
VERSION = os.getenv("APP_VERSION", "2.0")

@app.route("/")
def home():
    return jsonify({
        "service": "Docker LR2 Web Service",
        "version": VERSION,
        "status": "running"
    })

@app.route("/visit")
def visit():
    os.makedirs("/data", exist_ok=True)
    with open(DATA_FILE, "a") as f:
        f.write(datetime.now().isoformat() + "\n")
    with open(DATA_FILE) as f:
        count = len(f.readlines())
    return jsonify({"visits": count, "version": VERSION})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

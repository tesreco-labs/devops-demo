from flask import Flask, jsonify
from flask import Response
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total App Requests')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({"message": "DevOps Demo Running"})

# keep below function but in comment to demonstrate divide endpoint with division by zero error handled by telling the user that division by zero is not allowed instead of returning a 500 error
    

@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    REQUEST_COUNT.inc()
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    return jsonify({"result": a / b})


@app.route('/metrics-view')
def metrics_view():
    return f"<pre>{generate_latest().decode()}</pre>"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, render_template, jsonify
from anomaly_detection import train_model, detect_anomaly
from vectorstore import create_vectorstore
import os

app = Flask(__name__)

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Train the model and prepare the vectorstore on startup
vectorstore = create_vectorstore()
model = train_model(vectorstore)

@app.route("/")
def index():
    """
    Landing page for the project.
    """
    return render_template("index.html")

@app.route("/detection")
def detection():
    """
    Page for detecting anomalies in web server logs.
    """
    return render_template("detection.html")

@app.route("/detect", methods=["POST"])
def detect():
    """
    API to detect anomalies in web server access logs.
    """
    log_entry = request.json.get("log")
    result = detect_anomaly(log_entry, model, vectorstore)
    return jsonify({"anomaly": result})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

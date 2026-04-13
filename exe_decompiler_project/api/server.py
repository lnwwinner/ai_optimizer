from flask import Flask, request, jsonify
import os

from ai.malware_analyzer import MalwareAnalyzer
from ai.malware_classifier import MalwareClassifier
from ai.model_manager import ModelManager
from core.feature_extractor import FeatureExtractor

app = Flask(__name__)

analyzer = MalwareAnalyzer()
classifier = MalwareClassifier()
model_manager = ModelManager()
extractor = FeatureExtractor()

# Load model if exists
model = model_manager.load()
if model:
    classifier.model = model
    classifier.trained = True

@app.route("/analyze", methods=["POST"])
def analyze_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    filepath = os.path.join("temp", file.filename)
    os.makedirs("temp", exist_ok=True)
    file.save(filepath)

    try:
        report = analyzer.analyze_behavior(filepath)
        features = extractor.extract(filepath)

        combined = {**report, **features}

        prediction = classifier.predict(combined) if classifier.trained else "Model not trained"

        return jsonify({
            "report": report,
            "features": features,
            "prediction": prediction
        })

    finally:
        os.remove(filepath)

@app.route("/")
def home():
    return "AI Malware Analysis API Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

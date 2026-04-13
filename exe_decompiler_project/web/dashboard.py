from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
API_URL = "http://localhost:5000/analyze"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files.get("file")
        if file:
            files = {"file": (file.filename, file.stream, file.mimetype)}
            response = requests.post(API_URL, files=files)
            result = response.json()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(port=7000)

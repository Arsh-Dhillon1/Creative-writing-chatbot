from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests  # Added for HTTP requests
import random   # Added for random number generation

app = Flask(__name__)
CORS(app)  

API_KEY = "Cannot Show for Privacy Reason"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# Hardcoded credentials (replace with a database or secure method later)
VALID_USERNAME = "admin"
VALID_PASSWORD = "robot123"

@app.route("/")
def home():
    return render_template("index.html")  # Load the Creative Catalyst UI

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")  # Show login page
    elif request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False}), 401

@app.route("/generate_prompt", methods=["GET"])
def get_prompt():
    genre = request.args.get("genre", "sci-fi")  
    random_seed = random.randint(1, 100000)  

    payload = {
        "contents": [
            {"parts": [{"text": f"Generate a unique {genre} writing prompt. Seed: {random_seed}"}]}
        ]
    }

    response = requests.post(API_URL, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        prompt = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Error: No prompt generated")
        return jsonify({"prompt": prompt})
    else:
        return jsonify({"error": "Failed to fetch prompt"}), 500

if __name__ == "__main__":
    app.run(debug=True)

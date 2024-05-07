import random
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import time

from chat import get_response

app = Flask(__name__)
CORS(app)

GREETINGS = ['hi', 'hello', 'hey', 'greetings', 'howdy', 'yo']

GREETING_RESPONSES = [
    "Hey, I am vishwabot here to help you",
    "Hello! How can I assist you today?",
    "Hi there! What can I do for you?",
    "Hey! Vishwabot here. What's on your mind?",
    "What's up? How can I help?"
]

@app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    data = request.json
    text = data.get("message")

    if any(greeting in text.lower() for greeting in GREETINGS):
        time.sleep(5)
        response = random.choice(GREETING_RESPONSES)
    else:
        response = get_response(text)

    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

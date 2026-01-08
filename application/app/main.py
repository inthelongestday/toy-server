from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw")
def draw_numbers():
    numbers = sorted(random.sample(range(1, 46), 6))
    return jsonify(numbers)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
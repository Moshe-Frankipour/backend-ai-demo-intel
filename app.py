from flask import Flask, render_template
import random
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/random", methods=["GET"])
def rand():
    print("Generating random number")
    return str(random.randint(1, 100))


# Not a real endpoint, just for testing! NOT SECURE!
@app.route("/api/env/<key>", methods=["GET"])
def get_env(key):
    if key is None:
        return "Key not provided", 400

    val = os.environ.get(key)
    if val is None:
        return f"Key '{key}' not found", 404

    return val, 200


if __name__ == "__main__":
    app.run()

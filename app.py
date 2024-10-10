from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hi!"


@app.route("/error")
def error():
    1/0
    raise Exception("Testing sentry")

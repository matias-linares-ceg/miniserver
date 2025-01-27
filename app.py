from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hi!"

@app.route("/healthcheck")
def healthcheck():
    return "ok"

@app.route("/hello")
def hello():
    return "Hello, hello world!"
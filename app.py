from flask import Flask
import sentry_sdk

sentry_sdk.init(
    dsn="https://d48295d7afbd72525f78c7a3df3510da@sentry.cegdev.net/6",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
)

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi!"


@app.route("/error")
def error():
    raise Exception("Testing sentry")

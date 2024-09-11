FROM python:3.12-slim

WORKDIR /app

ADD app.py .

ENV PYTHONUSERBASE=/app

RUN pip install --user Flask sentry_sdk

CMD ["./bin/flask", "--app", "app", "run", "-h" , "0.0.0.0"]

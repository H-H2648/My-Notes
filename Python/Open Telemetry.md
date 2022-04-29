# basic turtorial:

For any services: flask, tornado, SQLAlchemy, etc., find it [here](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation). If not found, there is litterally nothing we can do.

When the code runs, it should automatically send the traces as long as we call .instrument() (may depend on the instrumentation).

For example, for flask app:

```
# app.py

import flask
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import requests

# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize automatic instrumentation with Flask
app = flask.Flask(__name__)

## instrumenting
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route("/")
def hello():
    return "Hello!"

if __name__=="__main__":
    app.run(debug=True)


# # Ingest trace context in whatever format Beehive sends (find out what format Beehive is sending data in)
# ASSUME W3C for now
# @app.route("/handle")
# def handle(req, res):
#     r = requests.get()
```

with `env.example` of

```
export OTEL_EXPORTER_OTLP_ENDPOINT="https://api.honeycomb.io"
export OTEL_EXPORTER_OTLP_HEADERS="x-honeycomb-team=_____YOUR_API_KEY_HERE____,x-honeycomb-dataset=demo-dataset" # note x-honeycomb-dataset is necessary and otherwise it sometimes won't send
export OTEL_SERVICE_NAME="flask-poc"
```

This will send the traces to honeycomb (assuming you register and use the API KEY correctly)

Flask + SQLAlchemy example:

```
# tracing.py
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcesso

# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

# Initialize automatic instrumentation with Flask and Requests
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
SQLAlchemyInstrumentor().instrument()

# Initializes sqlite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)

#constants to trace
SERIAL_NUMBER = os.environ.get("SERIAL_NUMBER")
REGISTRATION_NUMBER = os.environ.get("REGISTRATION_NUMBER")


def send_info(serial_num, reg_num, server_ver, pod_name, env):
    cur_span = trace.get_current_span()
    cur_span.set_attribute("SERIAL_NUMBER", serial_num)
    cur_span.set_attribute("REGISTRATION_NUMBER", reg_num)

# Very basic model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username


# So there is a table to query to
@app.before_first_request
def create_tables():
    db.create_all()


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route("/send")
def send_info():
    send_info(SERIAL_NUMBER, REGISTRATION_NUMBER)
    return "sent!"



# demo W3C propagation between services (tornado app must be running on port 8001)
@app.route("/fwd")
def fwd():
    r = requests.get("http://localhost:8001")
    return f"Forwarded: {r.content.decode('utf8')}"


# send some data in sqlite
@app.route("/sql_test/<username>/<email>")
def add_data(username, email):
    account = User(username=username, email=email)
    db.session.add(account)
    db.session.commit()
    return f"Created account?"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000", debug=True)
```

Tornado example

```
import os

import requests
import tornado.ioloop
import tornado.web
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import \
    OTLPSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.tornado import TornadoInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from tornado.options import define, options

# import requests

# Initialize tracing and an exporter that can send data to Honeycomb
provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)

define("port", default=8001, help="port to listen on")

TornadoInstrumentor().instrument()
RequestsInstrumentor().instrument()

#constants to trace
SERIAL_NUMBER = os.environ.get("SERIAL_NUMBER")
REGISTRATION_NUMBER = os.environ.get("REGISTRATION_NUMBER")

def send_info(serial_num, reg_num, server_ver, env):
    cur_span = trace.get_current_span()
    cur_span.set_attribute("SERIAL_NUMBER", serial_num)
    cur_span.set_attribute("REGISTRATION_NUMBER", reg_num)


class HelloWorldHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello from Tornado!")


class ForwardingHandler(tornado.web.RequestHandler):
    def get(self):
        r = requests.get("http://localhost:8000")
        self.write(f"Forwarded: {r.content.decode('utf8')}")

class SendingInfoHandler(tornado.web.RequestHandler):
    def get(self):
        send_info(SERIAL_NUMBER, REGISTRATION_NUMBER)
        self.write(f"sent")



if __name__ == "__main__":

    app = tornado.web.Application(
        [(r"/", HelloWorldHandler), (r"/fwd", ForwardingHandler), (r"/send", SendingInfoHandler)]
    )
    app.listen(options.port)

    print(f"Listening on http://localhost:{options.port}")
    tornado.ioloop.IOLoop.current().start()
```
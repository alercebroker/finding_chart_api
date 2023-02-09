from interface_adapters.controllers.controller import controller_get_chart
from flask import Flask, request

app = Flask(__name__, instance_relative_config=True)


@app.route("/")
def index():
    return "ALeRCE Finding Chart Generator"


@app.route("/get_chart")
def get_chart():
    return controller_get_chart(request)

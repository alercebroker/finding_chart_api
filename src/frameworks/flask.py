from src.interface_adapters.controllers.controller import (
    controller_get_chart,
)

import os
from flask import Flask, request

app = Flask(__name__, instance_relative_config=True)

STATIC_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
CSS_PATH = [
    os.path.join(STATIC_PATH, "css/template.css"),
    os.path.join(STATIC_PATH, "css/bootstrap.min.css"),
]

logo_path = os.path.join(STATIC_PATH, "img/logo.png")


@app.route("/")
def index():
    return "ALeRCE Finding Chart Generator"


@app.route("/get_chart")
def get_chart():
    return controller_get_chart(request, logo_path)


a = 0
if __name__ == "__main__":
    app.run(debug=True)

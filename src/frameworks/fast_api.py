import os
import uvicorn
from fastapi import FastAPI, Query, Depends

from src.interface_adapters.controllers.controller import (
    controller_get_chart,
)

from pydantic.dataclasses import dataclass

app = FastAPI(
    description="Simple findingchart for ZTF objects.",
    title="ALeRCE Finding Chart API",
    root_path=os.getenv("ROOT_PATH", "/"),
)


STATIC_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
CSS_PATH = [
    os.path.join(STATIC_PATH, "css/template.css"),
    os.path.join(STATIC_PATH, "css/bootstrap.min.css"),
]

logo_path = os.path.join(STATIC_PATH, "img/logo.png")


@app.get("/")
def index():
    return "ALeRCE Finding Chart Generator"


@dataclass
class GetChartInput:
    oid: str = Query(description="Object ID.")
    candid: float = Query(description="candid")


@app.get("/get_chart")
def get_chart(params: GetChartInput = Depends()):
    return controller_get_chart(params, logo_path)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)

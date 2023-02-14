import os
import uvicorn
from fastapi import FastAPI, Request, Query, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


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
TEMPLATES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "templates")

app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")


@app.get("/")
def index():
    return "ALeRCE Finding Chart Generator"


@dataclass
class GetChartInput:
    oid: str = Query(description="Object ID.")
    candid: str | None = Query(None, description="candid")


@app.get("/get_chart", response_class=HTMLResponse)
def get_chart(
    request: Request,
    params: GetChartInput = Depends(),
):
    return controller_get_chart(request, params, TEMPLATES_PATH)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)

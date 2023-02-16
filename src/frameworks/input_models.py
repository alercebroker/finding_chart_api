from fastapi import Query
from pydantic.dataclasses import dataclass


@dataclass
class GetChartInput:
    oid: str = Query(description="Object ID.")
    candid: str | None = Query(None, description="candid")
    size: int = Query(
        description="size of the image in pixels (width, height)", default=1000
    )

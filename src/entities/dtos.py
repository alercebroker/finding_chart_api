from dataclasses import dataclass


@dataclass
class RequestDto:
    oid: str
    size: str

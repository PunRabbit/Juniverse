from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=False)
class RequestDTO:
    OriginObject: Optional[object]
    Text: str
    Json: dict
    StatusCode: int

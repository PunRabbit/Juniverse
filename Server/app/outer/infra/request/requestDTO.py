from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=False)
class RequestDTO:
    originObject: Optional[object]
    text: str
    statusCode: int

from dataclasses import dataclass


@dataclass(frozen=False)
class ClovaTextDTO:
    text: str
    requestStatusCode: int

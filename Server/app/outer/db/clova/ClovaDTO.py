from dataclasses import dataclass


@dataclass(frozen=False)
class ClovaDTO:
    PureText: str
    BubbleText: str
    EffectText: str
    ThoughtText: str
    RequestTime: str
    StatusCode: int


from dataclasses import dataclass
from Server.app.infra.request.requestModule import PythonRequest


@dataclass(frozen=True)
class TestCaseList:
    PythonRequestTest: PythonRequest

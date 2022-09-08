from dataclasses import dataclass
from Server.app.outer.infra.request.requestsModule import PythonRequestsModule


@dataclass(frozen=True)
class TestCaseList:
    PythonRequestTest: PythonRequestsModule

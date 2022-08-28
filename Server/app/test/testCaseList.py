from dataclasses import dataclass
from Server.app.infra.request.pythonRequestsModule import PythonRequestsModule


@dataclass(frozen=True)
class TestCaseList:
    PythonRequestTest: PythonRequestsModule

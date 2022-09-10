from dataclasses import dataclass
from Server.app.test.SlackAlarmTest import SlackAlarmTest
from Server.app.test.ClovaRequestTest import ClovaRequestTest


@dataclass(frozen=True)
class TestCaseList:
    SlackAlarmTest: SlackAlarmTest = SlackAlarmTest()
    ClovaRequestTest: ClovaRequestTest = ClovaRequestTest()

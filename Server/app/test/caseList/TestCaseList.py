from dataclasses import dataclass
from Server.app.test.caseList.slack.SlackAlarmTest import SlackAlarmTest
from Server.app.test.caseList.clova.ClovaRequestTest import ClovaRequestTest


@dataclass(frozen=True)
class TestCaseList:
    SlackAlarmTest: SlackAlarmTest = SlackAlarmTest()
    ClovaRequestTest: ClovaRequestTest = ClovaRequestTest()

from dataclasses import dataclass
from Server.app.test.caseList.TestCaseAbstract import CustomCaseTest
from Server.app.test.caseList.slack.SlackAlarmTest import SlackAlarmTest
from Server.app.test.caseList.clova.ClovaRequestTest import ClovaRequestTest
from Server.app.test.caseList.mariaDB.MariaDBQueryTest import MariaDBQueryTest


@dataclass(frozen=True)
class TestCaseList:
    SlackAlarmTest: CustomCaseTest = SlackAlarmTest()
    ClovaRequestTest: CustomCaseTest = ClovaRequestTest()
    MariaDBQueryTest: CustomCaseTest = MariaDBQueryTest()

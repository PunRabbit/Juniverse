from unittest import TestCase
from Server.app.test.caseList.TestCaseAbstract import CustomCaseTest
from Server.app.infra.alarm.slack.SlackAlarm import SlackAlarmModule
from Server.app.infra.alarm.AlarmAbstract import AlarmModel


class SlackAlarmTest(TestCase, CustomCaseTest):
    def test_alarm_error(self):
        error_slack_test_instance: AlarmModel = SlackAlarmModule(target_channel="error")
        with self.assertRaises(Exception):
            error_slack_test_instance.send_alarm(message="test")

    def test_alarm_success(self):
        success_slack_test_instance: AlarmModel = SlackAlarmModule(target_channel="juniverse")
        success_slack_test_instance.send_alarm(message="Test Message Before Server Load")

    def test_alarm_success_with_template(self):
        success_slack_test_instance: AlarmModel = SlackAlarmModule(target_channel="juniverse")
        success_slack_test_instance.send_alarm_with_template(template="test_template",
                                                             message="테스트 성공입니다!")





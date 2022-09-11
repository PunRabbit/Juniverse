from unittest import TestCase
from Server.app.outer.alarm.slack.SlackAlarm import SlackAlarmModule
from Server.app.outer.alarm.AlarmAbstract import AlarmModel


class SlackAlarmTest(TestCase):
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





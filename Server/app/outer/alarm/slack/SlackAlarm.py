from slack_sdk import WebClient
from overrides import overrides
from Server.app.outer.alarm.AlarmAbstract import AlarmModel
from Server.app.core.compact.CompactConfig import CONFIG


class SlackAlarmModule(AlarmModel):
    __slots__ = [
        "_token",
        "_channel"
    ]

    def __init__(self, target_channel: str):
        self._token: str = CONFIG.SLACK.TOKEN
        self._channel: str = f"#{target_channel}"

    @overrides
    def send_alarm(self, message: str) -> None:
        self._create_client().chat_postMessage(channel=self._channel,
                                               text=message)

    @overrides
    def send_alarm_with_template(self, template: str, message: str) -> None:
        target_template: list = CONFIG.SLACK_TEMPLATES.TEST_TEMPLATES[template]
        target_template[2]["text"]["text"]: str = message
        self._create_client().chat_postMessage(channel=self._channel,
                                               blocks=target_template)

    def _create_client(self) -> WebClient:
        return WebClient(token=self._token)


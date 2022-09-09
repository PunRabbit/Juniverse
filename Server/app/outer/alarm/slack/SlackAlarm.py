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

    def _create_client(self) -> WebClient:
        return WebClient(token=self._token)


from overrides import overrides
from Server.app.infra.alarm.AlarmAbstract import AlarmModel


class TeamsAlarmModule(AlarmModel):
    __slots__ = [
        "_token",
        "_channel",
        "_bot_name",
        "_bot_image_path"
    ]

    def __init__(self, bot_name: str, bot_image_path: str):
        pass

    @overrides
    def send_alarm(self, message: str) -> None:
        pass

    @overrides
    def send_alarm_with_template(self, template: str, message: str) -> None:
        pass

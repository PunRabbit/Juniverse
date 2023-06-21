from abc import ABCMeta, abstractmethod


class AlarmModel(metaclass=ABCMeta):
    @abstractmethod
    def send_alarm(self, message: str) -> None:
        pass

    @abstractmethod
    def send_alarm_with_template(self, template: str, message: str) -> None:
        pass

from abc import ABCMeta, abstractmethod


class AlarmModel(metaclass=ABCMeta):
    @abstractmethod
    def send_alarm(self, message: str) -> None:
        pass

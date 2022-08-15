from abc import ABCMeta, abstractmethod
from Server.app.connection.clova.ClovaTextDTO import ClovaTextDTO


class ClovaTextOcrModel(metaclass=ABCMeta):
    @abstractmethod
    def request(self) -> ClovaTextDTO:
        pass


class ClovaRequestModel(metaclass=ABCMeta):
    @abstractmethod
    def request_to_clova(self) -> None:
        pass


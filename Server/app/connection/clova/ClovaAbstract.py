from abc import ABCMeta, abstractmethod
from Server.app.db.clova.ClovaDTO import ClovaDTO


class ClovaTextOcrModel(metaclass=ABCMeta):
    @abstractmethod
    def request(self) -> ClovaDTO:
        pass


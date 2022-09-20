from abc import ABCMeta, abstractmethod
from Server.app.infra.customRequest.RequestDTO import RequestDTO


class OCRModel(metaclass=ABCMeta):
    @abstractmethod
    def inference(self, image_path: str, image_format: str) -> RequestDTO:
        pass



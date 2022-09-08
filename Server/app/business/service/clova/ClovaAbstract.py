from abc import ABCMeta, abstractmethod
from Server.app.outer.infra.request.requestDTO import RequestDTO


class ClovaOCRModel(metaclass=ABCMeta):
    @abstractmethod
    def inference(self, image_path: str, image_format: str) -> RequestDTO:
        pass




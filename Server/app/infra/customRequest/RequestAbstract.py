from abc import ABCMeta, abstractmethod
from Server.app.infra.customRequest.RequestDTO import RequestDTO


class RequestModel(metaclass=ABCMeta):
    @abstractmethod
    def get_request(self, url: str) -> RequestDTO:
        pass

    @abstractmethod
    def post_request(self, url: str) -> RequestDTO:
        pass


class RequestCustomSettingModel(metaclass=ABCMeta):
    @abstractmethod
    def set_header(self, header: dict) -> None:
        pass

    @abstractmethod
    def set_body(self, body: dict) -> None:
        pass

    @abstractmethod
    def set_params(self, params: dict) -> None:
        pass

    @abstractmethod
    def set_auth(self, auth: dict) -> None:
        pass

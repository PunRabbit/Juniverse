from abc import ABCMeta, abstractmethod
from Server.app.infra.request.requestDTO import RequestDTO


class RequestModel(metaclass=ABCMeta):
    @abstractmethod
    def get_request(self) -> RequestDTO:
        pass

    @abstractmethod
    def post_request(self) -> RequestDTO:
        pass


class RequestCustomSettingModule(metaclass=ABCMeta):
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

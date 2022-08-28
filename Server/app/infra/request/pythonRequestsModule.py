import requests
from typing import Optional
from overrides import overrides
from Server.app.infra.request.abstract import RequestModel, RequestCustomSettingModel
from Server.app.infra.request.requestDTO import RequestDTO


class PythonRequestsModule(RequestModel, RequestCustomSettingModel):
    __slots__ = [
        "header",
        "body",
        "params",
        "auth",
        "url",
        "dto"
    ]

    def __init__(
            self,
            url: str,
            header: dict = None,
            body: dict = None,
            params: dict = None,
            auth: dict = None
    ):
        self.url: str = url
        self.header: dict = header
        self.body: dict = body
        self.params: dict = params
        self.auth: dict = auth
        self.dto: Optional[RequestDTO, None] = None

    @overrides
    def get_request(self) -> RequestDTO:
        if self._check_before_get_request() is True:
            response: requests.models.Response = requests.get(url=self.url)
        else:
            response: requests.models.Response = requests.get(
                url=self.url,
                headers=self.header,
                params=self.params
            )

        self.dto: RequestDTO = RequestDTO(
            OriginObject=response,
            Json=self._check_response_json_load(response=response),
            Text=response.text,
            StatusCode=response.status_code
        )

        return self.dto

    @overrides
    def post_request(self) -> RequestDTO:
        pass

    @overrides
    def set_header(self, header: dict) -> None:
        pass

    @overrides
    def set_body(self, body: dict) -> None:
        pass

    @overrides
    def set_params(self, params: dict) -> None:
        pass

    @overrides
    def set_auth(self, auth: dict) -> None:
        pass

    def _check_before_get_request(self) -> bool:
        if False not in [self._check_params(), self._check_auth()]:
            return False
        else:
            return True

    def _check_header(self) -> bool:
        if self.header is None:
            return False
        else:
            return True

    def _check_params(self) -> bool:
        if self.params is None:
            return False
        else:
            return True

    def _check_auth(self) -> bool:
        if self.auth is None:
            return False
        else:
            return True

    @classmethod
    def _check_response_json_load(cls, response: requests.models.Response) -> dict:
        try:
            response.json()
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {}


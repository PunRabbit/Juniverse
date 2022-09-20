import requests
from typing import Optional
from overrides import overrides
from Server.app.infra.customRequest.RequestAbstract import RequestModel
from Server.app.infra.customRequest.RequestDTO import RequestDTO


class RequestsModule(RequestModel):
    __slots__ = [
        "_params",
        "_data",
        "_headers"
    ]

    def __init__(self, params: Optional[dict] = None, data: Optional[dict] = None, headers: Optional[dict] = None):
        self._params: dict = params
        self._data: dict = data
        self._headers: dict = {
            "Content-Type": "application/json"
        } if headers is None else headers

    @overrides
    def get_request(self, url: str) -> RequestDTO:
        if self._params_none_check() is False:
            request_response: requests.Response = requests.get(
                url=url,
                params=self._params,
                headers=self._headers
            )
            return self._response_to_dto(init_response=request_response)
        else:
            request_response: requests.Response = requests.get(
                url=url,
                headers=self._headers
            )
            return self._response_to_dto(init_response=request_response)

    @overrides
    def post_request(self, url: str) -> RequestDTO:
        if self._data_none_check() is False:
            reqeust_response: requests.Response = requests.post(
                url=url,
                data=self._data,
                headers=self._headers
            )
            return self._response_to_dto(init_response=reqeust_response)
        else:
            request_response: requests.Response = requests.post(
                url=url,
                headers=self._headers
            )
            return self._response_to_dto(init_response=request_response)

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params: dict):
        self._params: dict = params

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers: dict):
        self._headers: dict = headers

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data: dict):
        self._data: dict = data

    @classmethod
    def _response_to_dto(cls, init_response: requests.Response) -> RequestDTO:
        request_dto: RequestDTO = RequestDTO(
            originObject=init_response,
            text=init_response.text,
            statusCode=init_response.status_code,
        )
        return request_dto

    def _params_none_check(self) -> bool:
        if self._params is None:
            return True
        else:
            return False

    def _data_none_check(self) -> bool:
        if self._data is None:
            return True
        else:
            return False

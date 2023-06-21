import httpx
from typing import Optional
from overrides import overrides
from Server.app.infra.customRequest.RequestAbstract import RequestModel
from Server.app.infra.customRequest.RequestDTO import RequestDTO


class HttpxModule(RequestModel):
    __slots__ = [
        "_params",
        "_data"
    ]

    def __init__(self, params: Optional[dict] = None, data: Optional[dict] = None):
        self._params: dict = params
        self._data: dict = data

    @overrides
    def get_request(self, url: str) -> RequestDTO:
        if self._params_none_check() is not False:
            request_response: httpx.Response = httpx.get(
                url=url,
                params=self._params
            )
            return self._response_to_dto(init_response=request_response)
        else:
            request_response: httpx.Response = httpx.get(
                url=url
            )
            return self._response_to_dto(init_response=request_response)

    @overrides
    def post_request(self, url: str) -> RequestDTO:
        if self._data_none_check() is not False:
            reqeust_response: httpx.Response = httpx.post(
                url=url,
                data=self._data
            )
            return self._response_to_dto(init_response=reqeust_response)
        else:
            request_response: httpx.Response = httpx.post(
                url=url
            )
            return self._response_to_dto(init_response=request_response)

    @classmethod
    def _response_to_dto(cls, init_response: httpx.Response) -> RequestDTO:
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

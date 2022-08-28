import httpx
from typing import Optional
from overrides import overrides
from Server.app.infra.request.requestDTO import RequestDTO
from Server.app.infra.request.abstract import RequestModel


class HttpxRequestModule(RequestModel):
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
        origin_response: httpx.Response = httpx.get(
            url=self.url
        )
        # Todo: Build Method
        pass

    @overrides
    def post_request(self) -> RequestDTO:
        # Todo: Build Method
        pass


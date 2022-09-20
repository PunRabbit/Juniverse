import time
import json
from overrides import overrides
from typing import Union
from Server.app.infra.ai.AiAbstract import OCRModel
from Server.app.infra.customRequest.RequestAbstract import RequestModel
from Server.app.infra.customRequest.pythonRequests.requestsModule import RequestsModule
from Server.app.infra.customRequest.RequestDTO import RequestDTO
from Server.app.core.compact.CompactConfig import CONFIG


class ClovaOCRRequestModule(OCRModel):
    __slots__ = [
        "_token",
        "_content_type",
        "_name",
        "_enable_table_detection",
        "_version",
        "_request_id",
        "_time_stamp",
        "_lang",
        "_url",
        "_request_module"
    ]

    def __init__(self, request_module: Union[RequestModel, RequestsModule]):
        self._token: str = CONFIG.CLOVA.USER_TOKEN
        self._content_type: str = "application/json"
        self._name: str = "TestUser"  # Have to Change this value into User(Writer) Information
        self._enable_table_detection: bool = False
        self._version: str = "V2"
        self._request_id: str = "TestId"  # Have to Change into Another User
        self._time_stamp: int = int(time.strftime('%y%m%d%H%M%S'))
        self._lang: str = "ko"
        self._url: str = CONFIG.CLOVA.USER_URL_PATH
        self._request_module: Union[RequestModel, RequestsModule] = request_module

    @overrides
    def inference(self, image_path: str, image_format: str) -> RequestDTO:
        payload: dict = self._build_payload(image_path=image_path, image_format=image_format)
        headers: dict = self._build_headers()
        self._implement_data_headers(data=payload, headers=headers)
        return self._request_module.post_request(url=self._url)

    def _implement_data_headers(self, data: dict, headers: dict):
        self._request_module.data = json.dumps(data)
        self._request_module.headers = headers

    def _build_payload(self, image_path: str, image_format: str) -> dict:
        payload: dict = dict(version=self._version,
                             requestId=self._request_id,
                             timestamp=self._time_stamp,
                             lang=self._lang,
                             images=[
                                 dict(format=image_format,
                                      url=image_path,
                                      name=self._name)
                             ],
                             enableTableDetection=self._enable_table_detection)

        return payload

    def _build_headers(self) -> dict:
        headers: dict = {
            f'{CONFIG.CLOVA.CLOVA_HEADER}': self._token,
            'Content-Type': self._content_type
        }
        return headers
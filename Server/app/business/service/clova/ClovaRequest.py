import time
import json
from overrides import overrides
from Server.app.business.service.clova.ClovaAbstract import ClovaOCRModel
from Server.app.outer.infra.request.abstract import RequestModel
from Server.app.core.compact.CompactConfig import CONFIG


class ClovaOCRRequest(ClovaOCRModel):
    __slots__ = [
        "_token",
        "_content_type",
        "_name",
        "_enable_table_detection",
        "_version",
        "_request_id",
        "_time_stamp",
        "_lang"
    ]

    def __init__(self, request_module: RequestModel):
        self._token: str = CONFIG.CLOVA.USER_TOKEN
        self._content_type: str = "application/json"
        self._name: str = "TestUser"  # Have to Change this value into User(Writer) Information
        self._enable_table_detection: bool = False
        self._version: str = "V2"
        self._request_id: str = "TestId"  # Have to Change into Another User
        self._time_stamp: int = int(time.strftime('%y%m%d%H%M%S'))
        self._lang: str = "ko"
        self._request_module: RequestModel = request_module

    @overrides
    def inference(self, image_path: str, image_format: str) -> RequestDTO:
        payload: str = self._build_payload(image_path=image_path, image_format=image_format)
        request_module: RequestModel = self._request_module

        pass

    def _build_payload(self, image_path: str, image_format: str) -> str:
        payload: str = json.dumps(
            dict(version=self._version,
                 requestId=self._request_id,
                 timestamp=self._time_stamp,
                 lang=self._lang,
                 images=[
                     dict(format=image_format,
                          url=image_path,
                          name=self._name)
                 ],
                 enableTableDetection=self._enable_table_detection)
        )
        return payload

    @classmethod
    def _build_headers(cls) -> dict:
        headers: dict = {
            'X-OCR-SECRET': CONFIG.CLOVA.USER_URL_PATH,
            'Content-Type': 'application/json'
        }
        return headers

from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from Server.app.business.service.clova.ClovaAbstract import ClovaOCRModel
from Server.app.business.service.clova.ClovaRequest import ClovaOCRRequestModule
from Server.app.outer.infra.request.requestsModule import RequestsModule
from Server.app.outer.infra.request.requestDTO import RequestDTO


class ClovaRequestTest(TestCase):
    def test_error_case(self):
        clova_error_instance: ClovaOCRModel = ClovaOCRRequestModule(request_module=RequestsModule())
        response_dto: RequestDTO = clova_error_instance.inference(image_path="1",
                                                                  image_format="2")
        self.assertEqual(response_dto.statusCode, 400)
        self.assertIsInstance(response_dto, RequestDTO)
        self.assertIsInstance(response_dto.statusCode, int)
        self.assertIsInstance(response_dto.text, str)
        self.assertIsInstance(response_dto.originObject, object)

    @patch("Server.app.test.ClovaRequestTest.RequestsModule")
    def test_error_case_with_no_real_reqeust(self, mock_request_module):
        mock_reqeust = mock_request_module.return_value
        mock_reqeust.post_request.return_value = RequestDTO(originObject="test",
                                                            text="test",
                                                            statusCode=777)
        clova_error_instance: ClovaOCRModel = ClovaOCRRequestModule(request_module=mock_reqeust)
        response_dto: RequestDTO = clova_error_instance.inference(image_path="1",
                                                                  image_format="2")
        self.assertEqual(response_dto.statusCode, 777)
        self.assertIsInstance(response_dto, RequestDTO)
        self.assertIsInstance(response_dto.statusCode, int)
        self.assertIsInstance(response_dto.text, str)


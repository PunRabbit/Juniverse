import sys
sys.path.append("/Users/jun/Juniverse")
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from slack_sdk import WebClient
from Server.app.core.compact.CompactConfig import CONFIG
# from Server.app.core.configs.BaseConfig import BASE_CONFIG
from Server.app.business.service.clova.ClovaRequest import ClovaOCRRequestModule
from Server.app.business.service.clova.ClovaAbstract import ClovaOCRModel
from Server.app.outer.infra.request.requestsModule import RequestsModule
from Server.app.outer.infra.request.abstract import RequestModel


app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.BASE.SERVER_ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

client: WebClient = WebClient(token=CONFIG.SLACK.TOKEN)

client.chat_postMessage(channel='#juniverse',
                        text='Test with Server Starting Flag')


request_module: RequestModel = RequestsModule()
test: ClovaOCRModel = ClovaOCRRequestModule(request_module=request_module)
print(test.inference(image_format="jpg", image_path="https://i.ibb.co/jZk15Tj/R1280x0-2.jpg"))


if __name__ == "__main__":
    uvicorn.run(
        CONFIG.BASE.DEFAULT_BRIDGE,
        host=CONFIG.BASE.SERVER_URL,
        port=CONFIG.BASE.SERVER_PORT,
        workers=CONFIG.BASE.SERVER_WORKER_NUM,
        reload=True
    )


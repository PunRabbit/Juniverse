import sys
sys.path.append("/Users/jun/Juniverse")
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from Server.app.core.configs.BaseConfig import BASE_CONFIG


app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[BASE_CONFIG.SERVER_ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(
        BASE_CONFIG.DEFAULT_BRIDGE,
        host=BASE_CONFIG.SERVER_URL,
        port=BASE_CONFIG.SERVER_PORT,
        workers=BASE_CONFIG.SERVER_WORKER_NUM,
        reload=True
    )


import sys
sys.path.append("./../../../Juniverse")
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from Server.app.core.base.BaseConfig import base_config


app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(
        base_config.DEFAULT_BRIDGE,
        host=base_config.SERVER_URL,
        port=base_config.SERVER_PORT,
        workers=base_config.SERVER_WORKER_NUM,
        reload=True
    )


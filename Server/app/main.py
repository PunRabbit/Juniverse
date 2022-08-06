import sys
sys.path.append("./../../../Juniverse")
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from Server.app.core.config import server_config

# test


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
        server_config.DEFAULT_BRIDGE,
        host=server_config.SERVER_URL,
        port=server_config.SERVER_PORT,
        workers=server_config.SERVER_WORKER_NUM,
        reload=True
    )


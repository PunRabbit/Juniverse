import sys
import os
sys.path.append(os.getcwd()[:-11])

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Server.app.core.compact.CompactConfig import CONFIG
from Server.app.test.compactRunner.CompactRunner import CompactRunnerModule


app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.BASE.SERVER_ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    CompactRunnerModule().start_test()
    uvicorn.run(
        CONFIG.BASE.DEFAULT_BRIDGE,
        host=CONFIG.BASE.SERVER_URL,
        port=CONFIG.BASE.SERVER_PORT,
        workers=CONFIG.BASE.SERVER_WORKER_NUM,
        reload=True
    )


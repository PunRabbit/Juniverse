import sys
import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

sys.path.append(os.getcwd()[:-11])

from Server.app.core.compact.CompactConfig import CONFIG
from Server.app.runner.MainRunner import main_run


app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.BASE.SERVER_ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    main_run()

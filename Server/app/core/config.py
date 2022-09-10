import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class Config(object):
    load_dotenv(
        dotenv_path="./.env",
        verbose=True
    )

    print(os.getenv("DEFAULT_BRIDGE"))

    DEFAULT_BRIDGE: str = os.getenv("DEFAULT_BRIDGE")
    SERVER_URL: str = os.getenv("SERVER_URL")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT"))
    SERVER_WORKER_NUM: int = int(os.getenv("SERVER_WORKER_NUM"))


server_config: Config = Config()

import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class BaseConfig(object):
    load_dotenv(
        dotenv_path="./.env",
        verbose=True
    )

    DEFAULT_BRIDGE: str = os.getenv("DEFAULT_BRIDGE")
    SERVER_URL: str = os.getenv("SERVER_URL")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT"))
    SERVER_WORKER_NUM: int = int(os.getenv("SERVER_WORKER_NUM"))


base_config: BaseConfig = BaseConfig()

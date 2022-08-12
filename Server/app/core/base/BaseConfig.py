import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseConfig(object):
    load_dotenv(
        dotenv_path="./.env",
        verbose=True
    )

    DEFAULT_BRIDGE: str = os.getenv("DEFAULT_BRIDGE")
    SERVER_URL: str = os.getenv("SERVER_URL")
    SERVER_PORT: int = int(os.getenv("SERVER_PORT"))
    SERVER_WORKER_NUM: int = int(os.getenv("SERVER_WORKER_NUM"))
    SERVER_BCRYPT_KEY: str = os.getenv("SERVER_BCRYPT_KEY")
    SERVER_ALLOW_ORIGIN: str = os.getenv("SERVER_ALLOW_ORIGIN")


BASE_CONFIG: BaseConfig = BaseConfig()

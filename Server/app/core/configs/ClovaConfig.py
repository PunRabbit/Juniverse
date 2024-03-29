import os
from dotenv import load_dotenv
from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass


@dataclass(frozen=True)
class ClovaConfig(ConfigClass):
    load_dotenv(
        dotenv_path="./.env",
        verbose=True
    )

    # Based on Naver Clova AI OCR Service
    USER_ID: str = os.getenv("CLOVA_USER_ID")
    USER_PWD: str = os.getenv("CLOVA_USER_PWD")
    USER_TOKEN: str = os.getenv("CLOVA_USER_TOKEN")
    USER_URL_PATH: str = os.getenv("CLOVA_USER_URL_PATH")

    # CLOVA Request Options
    CLOVA_HEADER: str = os.getenv("CLOVA_HEADER")




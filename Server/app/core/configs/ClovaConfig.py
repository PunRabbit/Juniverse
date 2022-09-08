import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass(frozen=True)
class ClovaConfig(object):
    load_dotenv(
        dotenv_path="./.env",
        verbose=True
    )

    # Based on Naver Clova AI OCR Service
    USER_ID: str = os.getenv("CLOVA_USER_ID")
    USER_PWD: str = os.getenv("CLOVA_USER_PWD")
    USER_TOKEN: str = os.getenv("CLOVA_USER_TOKEN")
    USER_URL_PATH: str = os.getenv("CLOVA_USER_URL_PATH")




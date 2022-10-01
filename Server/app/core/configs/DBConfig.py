import os
from dotenv import load_dotenv
from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass


@dataclass(frozen=True)
class DBConfig(ConfigClass):
    load_dotenv(
        dotenv_path="./.env",
        verbose=True
    )

    # MariaDB
    # Base Information
    MARIA_DB_PORT: int = int(os.getenv("MARIA_DB_PORT"))
    MARIA_DB_NAME: str = os.getenv("MARIA_DB_NAME")
    MARIA_DB_HOST: str = os.getenv("MARIA_DB_HOST")

    REDIS_DB_PORT: int = int(os.getenv("REDIS_DB_PORT"))
    REDIS_DB_HOST: str = os.getenv("REDIS_DB_HOST")
    REDIS_DB_NAME: str = os.getenv("REDIS_DB_NAME")

    # Base Option that Only for Develop
    MARIA_DB_DEVELOP_USER_NAME: str = os.getenv("MARIA_DB_DEVELOP_USER_NAME")
    MARIA_DB_DEVELOP_USER_PWD: str = os.getenv("MARIA_DB_DEVELOP_USER_PWD")
    MARIA_DB_DEVELOP_DB_NAME: str = os.getenv("MARIA_DB_DEVELOP_DB_NAME")

    # Separate Access Level
    MARIA_DB_USER_SELECT: str = os.getenv("MARIA_DB_USER_SELECT")
    MARIA_DB_USER_SELECT_PWD: str = os.getenv("MARIA_DB_USER_SELECT_PWD")
    MARIA_DB_USER_UPDATE: str = os.getenv("MARIA_DB_USER_UPDATE")
    MARIA_DB_USER_UPDATE_PWD: str = os.getenv("MARIA_DB_USER_UPDATE_PWD")
    MARIA_DB_USER_INSERT: str = os.getenv("MARIA_DB_USER_INSERT")
    MARIA_DB_USER_INSERT_PWD: str = os.getenv("MARIA_DB_USER_INSERT_PWD")
    MARIA_DB_USER_DELETE: str = os.getenv("MARIA_DB_USER_DELETE")
    MARIA_DB_USER_DELETE_PWD: str = os.getenv("MARIA_DB_USER_DELETE_PWD")

    # CONFIG FOR SQLALCHEMY
    SQLALCHEMY_ADDRESS: str = os.getenv("SQLALCHEMY_ADDRESS")


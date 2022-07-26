from dataclasses import dataclass


@dataclass
class DBConfig(object):
    # MariaDB
    # Base Information
    MARIA_DB_PORT: int = 0
    MARIA_DB_NAME: str = ""
    MARIA_DB_HOST: str = ""

    REDIS_DB_PORT: int = 0
    REDIS_DB_HOST: str = ""
    REDIS_DB_NAME: str = ""

    # Separate Access Level
    MARIA_DB_USER_SELECT: str = ""
    MARIA_DB_USER_SELECT_PWD: str = ""
    MARIA_DB_USER_UPDATE: str = ""
    MARIA_DB_USER_UPDATE_PWD: str = ""
    MARIA_DB_USER_INSERT: str = ""
    MARIA_DB_USER_INSERT_PWD: str = ""
    MARIA_DB_USER_DELETE: str = ""
    MARIA_DB_USER_DELETE_PWD: str = ""


db_config: DBConfig = DBConfig()

import pymysql
from Server.app.core.configs.DBConfig import DB_CONFIG
from Server.app.infra.db.DBAbstract import BaseDBSelectModel
from typing import List, Optional
from overrides import overrides


class MariaDBConnector(BaseDBSelectModel):
    __slots__ = [
        "port",
        "db_name",
        "host",
        "user",
        "__pwd",
        "connection"
    ]

    def __init__(self):
        self.port: int = DB_CONFIG.MARIA_DB_PORT
        self.db_name: str = DB_CONFIG.MARIA_DB_NAME
        self.host: str = DB_CONFIG.MARIA_DB_HOST
        self.user: str = DB_CONFIG.MARIA_DB_USER_SELECT
        self._pwd: str = DB_CONFIG.MARIA_DB_USER_SELECT_PWD
        self.connection: Optional[pymysql.connect, None] = None
        self.connect()

    @overrides
    def connect(self) -> None:
        self.connection: pymysql.connect = pymysql.connect(
            host=self.host,
            db=self.db_name,
            port=self.port,
            user=self.user,
            passwd=self.__pwd
        )
        assert self._connection_check() is True,\
            "Connection is Empty, Please Check MariaDB Connection"

    @overrides
    def single_select(self, query: str) -> str:
        pass

    @overrides
    def multi_select(self, query: str) -> List[str]:
        pass

    def _connection_check(self) -> bool:
        if self.connection is None:
            return True
        else:
            return False

    @property
    def _pwd(self) -> None:
        return None

    @_pwd.setter
    def _pwd(self, pwd: str) -> None:
        self.__pwd: str = pwd


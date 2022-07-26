import pymysql
from Server.app.core.db.DBConfig import db_config
from Server.app.db.base.BaseDBAbstract import BaseDBSelectModel,\
    BaseDBDeleteModel, BaseDBInsertModel, BaseDBUpdateModel
from typing import List, Optional


class MariaDBConnector(BaseDBSelectModel):
    def __init__(self):
        self.port: int = db_config.MARIA_DB_PORT
        self.db_name: str = db_config.MARIA_DB_NAME
        self.host: str = db_config.MARIA_DB_HOST
        self.user: str = db_config.MARIA_DB_USER_SELECT
        self.pwd: str = db_config.MARIA_DB_USER_SELECT_PWD
        self.connection: Optional[pymysql.connect, None] = None
        self.connect()

    def connect(self) -> None:
        self.connection: pymysql.connect = pymysql.connect(
            host=self.host,
            db=self.db_name,
            port=self.port,
            user=self.user,
            passwd=self.pwd
        )
        assert self._connection_check() is True,\
            "Connection is Empty, Please Check MariaDB Connection"

    def single_select(self, query: str) -> str:
        pass

    def multi_select(self, query: str) -> List[str]:
        pass

    def _connection_check(self) -> bool:
        if self.connection is None:
            return True
        else:
            return False


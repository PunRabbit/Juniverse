import pymysql
from overrides import overrides
from typing import Union, Any, List, Optional, Tuple
from Server.app.core.compact.CompactConfig import CONFIG
from Server.app.infra.db.DBAbstract import QueryDBModel, DBConnection
from Server.app.infra.db.mariaDB.MariaDBDecorator import check_connection


class MariaDBQueryModule(QueryDBModel):
    __slots__ = [
        "connection"
    ]

    def __init__(self):
        self.connection: Optional[pymysql.Connection] = None

    # Todo: Change this method when in time of Release.
    # Set Default Value of db_name arg is Only for Develop.
    @overrides
    def create_connection(self, db_name: str = CONFIG.DB.MARIA_DB_NAME) -> Union[DBConnection, Any]:
        self.connection: pymysql.Connection = pymysql.connect(
            host=CONFIG.DB.MARIA_DB_HOST,
            port=CONFIG.DB.MARIA_DB_PORT,
            user=CONFIG.DB.MARIA_DB_DEVELOP_USER_NAME,
            password=CONFIG.DB.MARIA_DB_DEVELOP_USER_PWD,
            database=db_name
        )
        return self.connection

    @check_connection
    @overrides
    def select(self, query: str) -> List[tuple]:
        cursor: pymysql.Connection.cursor = self.connection.cursor()
        cursor.execute(query=query)
        origin_data: tuple = cursor.fetchall()
        data: List[tuple] = list(origin_data)
        return data

    @check_connection
    @overrides
    def insert(self, query: str) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query=query)
                self.connection.commit()
        finally:
            self.connection.close()

    @check_connection
    @overrides
    def delete(self, query: str) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query=query)
                self.connection.commit()
        finally:
            self.connection.close()

    @check_connection
    @overrides
    def update(self, query: str) -> None:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query=query)
                self.connection.commit()
        finally:
            self.connection.close()









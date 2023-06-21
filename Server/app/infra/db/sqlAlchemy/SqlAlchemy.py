import sqlalchemy
from overrides import overrides
from typing import Union, Any, List, Optional, Tuple
from Server.app.core.compact.CompactConfig import CONFIG
from Server.app.infra.db.DBAbstract import QueryDBModel, DBConnection


class SqlAlchemyQueryModule(QueryDBModel):
    __slots__ = [
        "connection"
    ]

    def __init__(self):
        self.connection: Optional[sqlalchemy.engine.base.Connection] = None
        self.metadata: Optional[sqlalchemy.MetaData] = None
        self.engine: Optional[sqlalchemy.engine.base.Engine] = None

    @overrides
    def create_connection(self, db_name: str = "DEFAULT DB") -> Union[DBConnection, Any]:
        self.engine: sqlalchemy.engine.base.Engine = sqlalchemy.create_engine(CONFIG.DB.SQLALCHEMY_ADDRESS)
        self.connection: sqlalchemy.engine.base.Connection = self.engine.connect()
        self.metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()

        return self.connection

    @overrides
    def select(self, query: str) -> List[tuple]:
        execute_state: sqlalchemy.engine.cursor.CursorResult = self.connection.execute(statement=query)
        result_set: List[tuple] = execute_state.fetchall()

        return result_set

    @overrides
    def insert(self, query: str) -> None:
        self._query_executor(query=query)

    @overrides
    def delete(self, query: str) -> None:
        self._query_executor(query=query)

    @overrides
    def update(self, query: str) -> None:
        self._query_executor(query=query)

    def _query_executor(self, query: str) -> None:
        execute_state: sqlalchemy.engine.cursor.CursorResult = self.connection.execute(statement=query)
        execute_state.close()




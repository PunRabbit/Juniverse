from unittest import TestCase
from typing import List
from Server.app.test.caseList.TestCaseAbstract import CustomCaseTest
from Server.app.infra.db.DBAbstract import QueryDBModel
from Server.app.infra.db.mariaDB.MariaDB import MariaDBQueryModule


class MariaDBQueryTest(TestCase, CustomCaseTest):
    def test_create_connection_with_name(self):
        test_db_connection: QueryDBModel = MariaDBQueryModule()
        test_db_connection.create_connection(db_name='webtoon_test')

    def test_create_connection_no_name(self):
        test_db_connection: QueryDBModel = MariaDBQueryModule()
        test_db_connection.create_connection()

    def test_select_query(self):
        test_db_connection: QueryDBModel = MariaDBQueryModule()
        test_query: str = "SELECT * FROM User"
        result: List[tuple] = test_db_connection.select(query=test_query)
        self.assertEqual(type(result), list)

    def test_insert_query(self):
        test_db_connection: QueryDBModel = MariaDBQueryModule()
        test_query: str = "INSERT INTO User (test) VALUES ('test')"
        test_db_connection.insert(query=test_query)

    def test_update_query(self):
        test_db_connection: QueryDBModel = MariaDBQueryModule()
        test_query: str = "UPDATE User SET test = 'test2' WHERE test = 'test'"
        test_db_connection.update(query=test_query)

    def test_delete_query(self):
        test_db_connection: QueryDBModel = MariaDBQueryModule()
        test_query: str = "DELETE FROM User WHERE test = 'test2'"
        test_db_connection.delete(query=test_query)


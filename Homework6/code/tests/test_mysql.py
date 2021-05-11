import pytest

from mysql.builder import MySQLBuilder


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestMySQL(MySQLBase):

    def test_number_of_all_requests(self):
        self.number_of_all_requests = self.mysql_builder.create_number_of_all_requests()
        number_of_all_requests = self.mysql.execute_query("SELECT * FROM table_number_of_all_requests")
        assert len(number_of_all_requests) == 1

    def test_number_of_requests_by_type(self):
        self.number_of_requests_by_type = self.mysql_builder.create_number_of_requests_by_type()
        number_of_requests_by_type = self.mysql.execute_query("SELECT * FROM table_number_of_requests_by_type")
        assert len(number_of_requests_by_type) == 5

    def test_top_10_of_most_frequent_requests(self):
        self.top_10_of_most_frequent_requests = self.mysql_builder.create_top_10_of_most_frequent_requests()
        top_10_of_most_frequent_requests = self.mysql.execute_query("SELECT * FROM table_top_10_of_most_frequent_requests")
        assert len(top_10_of_most_frequent_requests) == 10

    def test_top_5_of_biggest_requests_with_4xx_status(self):
        self.mysql_builder.create_top_5_of_biggest_requests_with_4xx_status()
        top_5_of_biggest_requests_with_4xx_status = self.mysql.execute_query("SELECT * FROM table_top_5_of_biggest_requests_with_4xx_status")
        assert len(top_5_of_biggest_requests_with_4xx_status) == 5

    def test_top_5_of_users_by_quantity_with_5xx_status(self):
        self.mysql_builder.create_top_5_of_users_by_quantity_with_5xx_status()
        top_5_of_users_by_quantity_with_5xx_status = self.mysql.execute_query("SELECT * FROM table_top_5_of_users_by_quantity_with_5xx_status")
        assert len(top_5_of_users_by_quantity_with_5xx_status) == 5

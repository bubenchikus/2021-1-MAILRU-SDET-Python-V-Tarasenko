import pytest

from mysql.builder import MySQLBuilder
from mysql.models import NumberOfAllRequests, NumberOfRequestsByType, Top10OfMostFrequentRequests, \
    Top5OfBiggestRequestsWith4XXStatus, Top5OfUsersByQuantityWith5XXStatus


class MySQLBase:

    def prepare(self):
        pass

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.mysql_builder = MySQLBuilder(mysql_client)

        self.prepare()


class TestMySQL(MySQLBase):

    def template(self, model):

        if not self.mysql.session.query(model).first():
            self.mysql_builder.create_all_tables()
            self.mysql.connect()

        return self.mysql.session.query(model).all()

    def test_number_of_all_requests(self):
        model = NumberOfAllRequests
        number_of_all_requests = self.template(model)
        assert len(number_of_all_requests) == 1

    def test_number_of_requests_by_type(self):
        model = NumberOfRequestsByType
        number_of_requests_by_type = self.template(model)
        assert len(number_of_requests_by_type) == 5

    def test_top_10_of_most_frequent_requests(self):
        model = Top10OfMostFrequentRequests
        top_10_of_most_frequent_requests = self.template(model)
        assert len(top_10_of_most_frequent_requests) == 10

    def test_top_5_of_biggest_requests_with_4xx_status(self):
        model = Top5OfBiggestRequestsWith4XXStatus
        top_5_of_biggest_requests_with_4xx_status = self.template(model)
        assert len(top_5_of_biggest_requests_with_4xx_status) == 5

    def test_top_5_of_users_by_quantity_with_5xx_status(self):
        model = Top5OfUsersByQuantityWith5XXStatus
        top_5_of_users_by_quantity_with_5xx_status = self.template(model)
        assert len(top_5_of_users_by_quantity_with_5xx_status) == 5

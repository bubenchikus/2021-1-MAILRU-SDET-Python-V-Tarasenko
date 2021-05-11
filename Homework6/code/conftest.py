import pytest

from mysql.client import MysqlClient

USER = 'root'
PASSWORD = 'pass'
DB_NAME = 'TEST_PYTHON'


@pytest.fixture(scope='function')
def mysql_client():
    mysql_client = MysqlClient(user=USER, password=PASSWORD, db_name=DB_NAME)
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user=USER, password=PASSWORD, db_name=DB_NAME)
        mysql_client.recreate_db()

        mysql_client.connect()
        name_list = ['table_number_of_all_requests',
                     'table_number_of_requests_by_type',
                     'table_top_10_of_most_frequent_requests',
                     'table_top_5_of_biggest_requests_with_4xx_status',
                     'table_top_5_of_users_by_quantity_with_5xx_status']
        mysql_client.create_multiple_tables_by_name(name_list)

        mysql_client.connection.close()

import pytest

from utils.builder import Builder


class ApiBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, credentials):
        self.builder = Builder()
        self.api_client = api_client

    @pytest.fixture(scope='function')
    def login_default(self, api_client, credentials):
        self.api_client.post_login(*credentials)

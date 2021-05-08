import pytest
from utilities.builder import Builder


class ApiBase:

    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client, credentials):
        self.builder = Builder()
        self.api_client = api_client
        if self.authorize:
            self.api_client.post_login(*credentials)

    @pytest.fixture(scope='function')
    def auto_create_campaign(self):
        self.api_client.post_create_campaign()
        yield

    @pytest.fixture(scope='function')
    def auto_create_segment(self):
        self.api_client.post_create_segment()

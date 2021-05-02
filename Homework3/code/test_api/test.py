import pytest

from test_api.base import ApiBase


@pytest.mark.API
class TestApi(ApiBase):

    def test_create_campaign(self, auto_delete_campaign):
        self.api_client.post_create_campaign()

    def test_create_segment(self):
        self.api_client.post_create_segment()

    def test_delete_segment(self, auto_create_segment):
        self.api_client.post_delete_segment()

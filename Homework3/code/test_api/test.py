import pytest

from api.client import InvalidLoginException
from test_api.base import ApiBase


@pytest.mark.API
class TestApiLogin(ApiBase):

    def test_valid_login(self, login_default):
        pytest.fail('Login unexpectedly succeeded')

    def test_invalid_login(self):
        with pytest.raises(InvalidLoginException):
            self.api_client.post_login('ghtdh54423', 'wetehuililh5536')
            pytest.fail('Login unexpectedly succeeded')


@pytest.mark.API
class TestApiNewCampaign(ApiBase):
    def test_new_campaign(self, login_default):
        self.api_client.post_new_campaign()


@pytest.mark.API
class TestApiNewSegment(ApiBase):
    def test_new_segment(self):
        self.api_client.post_new_segment()
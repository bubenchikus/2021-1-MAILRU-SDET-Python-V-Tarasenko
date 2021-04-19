import pytest

from base import BaseCase


@pytest.mark.UI
class TestLoginWindow(BaseCase):

    def test_login_positive(self, login_default):
        assert self.driver.current_url == 'https://target.my.com/dashboard'

    @pytest.mark.parametrize('uid', ['invalid-password', 'mail-several'])
    def test_login_negative(self, uid):
        self.base_page.login_fill(uid)
        assert 'Invalid login or password' in self.driver.page_source


@pytest.mark.UI
class TestNewCampaign(BaseCase):

    def test_new_campaign(self, open_and_delete_campaigns):
        name = 'My Campaign Name'
        self.new_campaign_page.new_campaign_full_process(name=name)
        self.main_page.go_to_campaign_list_page()
        assert name in self.driver.page_source


@pytest.mark.UI
class TestNewSegment(BaseCase):

    name = 'My Segment Name'

    def test_add_segment(self, create_and_delete_segments, name=name):
        self.segments_page.create_segment(name)
        assert name in self.driver.page_source

    def test_delete_segment(self, create_segment, name=name):
        self.segments_page.delete_segments()
        assert (name not in self.driver.page_source)

import pytest
import os

from CODE.TEST.base import BaseCase


@pytest.mark.UI
# @pytest.mark.skip('SKIP')
class TestLoginWindow(BaseCase):

    def test_login_positive(self, login_default):
        pass

    @pytest.mark.parametrize('uid', ['invalid-password', 'empty-mail'])
    def test_login_negative(self, uid):
        self.base_page.login_fill(uid)


@pytest.mark.UI
# @pytest.mark.skip('SKIP')
class TestNewCampaign(BaseCase):
    def test_new_campaign_start(self, open_campaign_page):
        pass

    def test_new_campaign_full_process(self, open_campaign_page, repo_root):
        self.new_campaign_page.choose_goal()
        self.new_campaign_page.fill_url()
        self.new_campaign_page.fill_name('My Campaign Name')

        self.new_campaign_page.set_sex()
        self.new_campaign_page.set_age()
        self.new_campaign_page.set_geography()
        self.new_campaign_page.set_behavior()
        self.new_campaign_page.set_interests()
        self.new_campaign_page.set_context()
        self.new_campaign_page.set_segments()
        self.new_campaign_page.set_schedule_of_display()
        self.new_campaign_page.set_schedule_of_company()
        self.new_campaign_page.set_model()

        self.new_campaign_page.choose_format()

        path1 = os.path.join(repo_root, "UPLOAD", "goose1.jpg")
        path2 = os.path.join(repo_root, "UPLOAD", "goose2.jpg")
        self.new_campaign_page.set_all_slides(path1, path2)
        self.new_campaign_page.save_campaign()

        self.main_page.check_creation('My Campaign Name')


@pytest.mark.UI
class TestSegments(BaseCase):

    def test_add_segments(self, create_segment):
        pass

    def test_delete_segments(self, create_segment):
        self.segments_page.delete_segment()

    def test_check_segments(self, create_segment):
        self.segments_page.check_segment('')




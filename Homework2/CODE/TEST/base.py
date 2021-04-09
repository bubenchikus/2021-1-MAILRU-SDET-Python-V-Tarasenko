import pytest
from _pytest.fixtures import FixtureRequest

from CODE.UI.pages.base_page import BasePage
from CODE.UI.pages.main_page import MainPage
from CODE.UI.pages.new_campaign_page import NewCampaignPage
from CODE.UI.pages.segments_page import SegmentsPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.new_campaign_page: NewCampaignPage = request.getfixturevalue('new_campaign_page')
        self.segments_page: SegmentsPage = request.getfixturevalue('segments_page')

        self.logger.debug('Initial setup done!')

    @pytest.fixture(scope='function')
    def login_default(self):
        self.base_page.login_fill('default')
        yield MainPage

    @pytest.fixture(scope='function')
    def open_campaign_page(self, login_default):
        self.main_page.go_to_campaign_page()

    @pytest.fixture(scope='function')
    def create_segment(self, login_default):
        self.main_page.go_to_segments_page()
        self.segments_page.create_segment()


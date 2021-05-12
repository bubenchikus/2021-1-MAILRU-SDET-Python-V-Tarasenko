import pytest
from _pytest.fixtures import FixtureRequest
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.chat_page import ChatPage
from ui.pages.settings_page import SettingsPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest, logger, ui_report):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.chat_page: ChatPage = request.getfixturevalue('chat_page')
        self.settings_page: SettingsPage = request.getfixturevalue('settings_page')

        self.logger.debug('Initial setup done!')

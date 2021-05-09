from ui.pages.main_page import MainPage
from ui.locators.locators import SettingsLocators
import os
import re


class SettingsPage(MainPage):

    locators = SettingsLocators()

    def open_news_source_settings(self):
        self.enter_settings()
        self.swipe_up_to_element(self.locators.NEWS_SOURCE, 2)
        self.click_for_android(self.locators.NEWS_SOURCE)

    def choose_news_source(self, source):
        self.open_news_source_settings()
        news_locator = self.find_by_text(source)
        self.click_for_android(news_locator)

    def open_about(self):
        self.enter_settings()
        self.swipe_up_to_element(self.locators.ABOUT, 3)
        self.click_for_android(self.locators.ABOUT)

    @staticmethod
    def extract_version():
        path = os.path.abspath(os.path.join(os.path.abspath(__file__), '../../..', 'app'))
        filename = os.listdir(path)[0]
        version = re.search(r'v(([0-9]+)\.)*', filename)[0][1:-1]
        return version


from ui.pages.base_page import BasePage
from ui.locators.locators import SettingsLocators


class SettingsPage(BasePage):

    locators = SettingsLocators()

    def open_news_source_settings(self):
        self.swipe_up_to_element(self.locators.NEWS_SOURCE, 2)
        self.click_for_android(self.locators.NEWS_SOURCE)

    def set_vesti_fm(self):
        self.open_news_source_settings()
        self.click_for_android(self.locators.VESTI_FM)

    def open_about(self):
        self.swipe_up_to_element(self.locators.ABOUT, 3)
        self.click_for_android(self.locators.ABOUT)

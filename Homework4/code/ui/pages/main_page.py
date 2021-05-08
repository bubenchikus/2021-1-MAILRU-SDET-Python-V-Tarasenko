from ui.pages.base_page import BasePage
from ui.locators.locators import MainLocators


class MainPage(BasePage):

    locators = MainLocators()

    def enter_chat(self):
        self.click_for_android(self.locators.ENTER_CHAT)

    def enter_settings(self):
        self.click_for_android(self.locators.ENTER_SETTINGS)

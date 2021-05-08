from ui.pages.base_page import BasePage
from ui.locators.locators import ChatLocators


class ChatPage(BasePage):

    locators = ChatLocators()

    def enter_message(self, text):
        self.find(self.locators.MESSAGE_FIELD).send_keys(text)

    def enter_and_send_message(self, text):
        self.enter_message(text)
        self.click_for_android(self.locators.SEND_FIELD)

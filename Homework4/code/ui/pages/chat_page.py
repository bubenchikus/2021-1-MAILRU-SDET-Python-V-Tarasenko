from ui.pages.main_page import MainPage
from ui.locators.locators import ChatLocators


class ChatPage(MainPage):

    locators = ChatLocators()

    def enter_message(self, text):
        self.find(self.locators.MESSAGE_FIELD).send_keys(text)

    def enter_and_send_message(self, text):
        self.enter_message(text)
        self.click_for_android(self.locators.SEND_FIELD)

    def first_message(self, text):
        self.enter_chat()
        self.enter_and_send_message(text)

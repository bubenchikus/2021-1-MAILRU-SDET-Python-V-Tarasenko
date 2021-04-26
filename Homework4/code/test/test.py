import pytest
from base import BaseCase


class TestMarussia(BaseCase):

    @pytest.mark.AndroidUI
    def test_command(self):
        self.main_page.enter_chat()
        self.chat_page.enter_and_send_message('Russia')

        assert self.base_page.find(self.chat_page.locators.FACT_CARD)

        self.chat_page.swipe_and_click_population()

        assert self.base_page.find(self.chat_page.locators.POPULATION_RESPONSE)

    @pytest.mark.AndroidUI
    def test_calculator(self):
        self.main_page.enter_chat()
        self.chat_page.enter_and_send_message('5+8/2')

        assert self.base_page.find(self.chat_page.locators.CALCULATOR_RESPONSE)

    @pytest.mark.AndroidUI
    def test_news_source(self):
        self.main_page.enter_settings()
        self.settings_page.set_vesti_fm()

        assert self.base_page.find(self.settings_page.locators.CHECK)

    @pytest.mark.AndroidUI
    def test_settings(self):
        self.main_page.enter_settings()
        self.settings_page.open_about()

        assert self.base_page.find(self.settings_page.locators.VERSION).text == 'Версия 1.39.1'

        assert self.base_page.find(self.settings_page.locators.RIGHTS_RESERVED)


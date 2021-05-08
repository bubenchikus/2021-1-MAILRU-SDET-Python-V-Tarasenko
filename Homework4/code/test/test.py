import pytest
from base import BaseCase
import os
import re


class TestMarussia(BaseCase):

    @pytest.mark.AndroidUI
    def test_command(self):
        self.main_page.enter_chat()
        self.chat_page.enter_and_send_message('Russia')

        assert self.base_page.find(self.base_page.find_by_text('государство в Восточной Европе'))

        self.chat_page.swipe_and_click_by_text('население россии')

        assert self.base_page.find(self.base_page.find_by_text('146 млн.'))

    @pytest.mark.AndroidUI
    def test_calculator(self):
        self.main_page.enter_chat()
        self.chat_page.enter_and_send_message('5+8/2')

        assert self.base_page.find(self.base_page.find_by_text('9'))

    @pytest.mark.AndroidUI
    def test_news_source(self):
        self.main_page.enter_settings()
        self.settings_page.open_news_source_settings()

        news_locator = self.base_page.find_by_text('Вести FM')

        self.base_page.click_for_android(news_locator)

        assert self.base_page.find(self.settings_page.locators.CHECK)

        self.settings_page.click_for_android(self.settings_page.locators.BACK)
        self.settings_page.click_for_android(self.settings_page.locators.BACK)
        self.main_page.enter_chat()
        self.chat_page.enter_and_send_message('News')

        assert self.base_page.find(news_locator)

    path = os.path.abspath(os.path.join(os.path.abspath(__file__), '../..', 'app'))
    print('PATH', path)
    filename = os.listdir(path)[0]
    version = re.search(r'v(([0-9]+)\.)*', filename)[0][1:-1]

    @pytest.mark.AndroidUI
    def test_settings(self):
        self.main_page.enter_settings()
        self.settings_page.open_about()

        assert self.base_page.find(self.base_page.find_by_text(f'Версия {self.version}'))

        assert self.base_page.find(self.base_page.find_by_text('Все права защищены.'))

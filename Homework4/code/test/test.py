import pytest
from base import BaseCase
import os
import re


class TestMarussia(BaseCase):

    @pytest.mark.AndroidUI
    def test_command(self):
        self.chat_page.first_message('Russia')

        assert self.base_page.find(self.base_page.find_by_text('государство в Восточной Европе'))

        self.chat_page.swipe_and_click_by_text('население россии')

        assert self.base_page.find(self.base_page.find_by_text('146 млн.'))

    @pytest.mark.AndroidUI
    def test_calculator(self):
        self.chat_page.first_message('5+8/2')

        assert self.base_page.find(self.base_page.find_by_text('9'))

    @pytest.mark.AndroidUI
    def test_news_source(self):
        source = 'Вести FM'
        self.settings_page.choose_news_source(source)

        assert self.base_page.find(self.settings_page.locators.CHECK)

        self.base_page.go_back(2)
        self.chat_page.first_message('News')

        assert self.base_page.find(self.base_page.find_by_text(source))

    @pytest.mark.AndroidUI
    def test_settings(self):
        self.settings_page.open_about()

        version = self.settings_page.extract_version()
        assert self.base_page.find(self.base_page.find_by_text(f'Версия {version}'))

        assert self.base_page.find(self.base_page.find_by_text('Все права защищены.'))

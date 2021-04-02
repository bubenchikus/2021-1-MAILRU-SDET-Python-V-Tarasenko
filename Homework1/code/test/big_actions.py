import pytest
import time

import user_data as udata
from ui.locators import basic_locators as BL
from base import BaseCase


class BigActions(BaseCase):

    def login_page(self):
        self.get_page("https://target.my.com")
        self.click(BL.LOGIN_START_LOCATOR)

    def login_fill(self, user_code):
        self.login_page()
        self.fill_field(BL.LOGIN_MAIL_LOCATOR, udata.login[user_code][0])
        self.fill_field(BL.LOGIN_PASSWORD_LOCATOR, udata.login[user_code][1])
        self.click(BL.LOGIN_SUBMIT_LOCATOR)

    @pytest.fixture(scope='function')
    def login_default(self):
        self.login_fill('default')
        self.wait_load(BL.DASHBOARD_CONTENT)

    def logout_buttons(self):
        self.click(BL.LOGOUT_START_LOCATOR)
        time.sleep(0.5)
        self.click(BL.LOGOUT_BUTTON_LOCATOR)

    def change_fill(self, user_code):
        self.get_page("https://target.my.com/profile/contacts")

        self.fill_field(BL.CHANGE_FIO_LOCATOR, udata.change[user_code][0])
        self.fill_field(BL.CHANGE_PHONE_LOCATOR, udata.change[user_code][1])
        self.fill_field(BL.CHANGE_MAIL_LOCATOR, udata.change[user_code][2])

        self.click(BL.CHANGE_SAVE_LOCATOR)

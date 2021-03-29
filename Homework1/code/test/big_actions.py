import user_data as udata
from ui.locators import basic_locators as BL

from base import BaseCase

import pytest


class BigActions(BaseCase):

    def login_page(self):
        self.driver.get("https://target.my.com")
        self.click(BL.LOGIN_START_LOCATOR)

    def login_fill(self, user_code):
        self.login_page()
        self.fill_field(BL.LOGIN_MAIL_LOCATOR, udata.login[user_code][0])
        self.fill_field(BL.LOGIN_PASSWORD_LOCATOR, udata.login[user_code][1])
        self.click(BL.LOGIN_SUBMIT_LOCATOR)

    @pytest.fixture(scope='function')
    def login_default(self):
        self.login_fill('default')

    @pytest.fixture(scope='function')
    def logout_default(self):
        yield
        self.click(BL.LOGOUT_START_LOCATOR)
        self.click(BL.LOGOUT_BUTTON_LOCATOR)

    def change_page(self):
        self.driver.get("https://target.my.com/profile/contacts")

    def change_fill(self, user_code):
        self.change_page()
        self.fill_field(BL.CHANGE_FIO_LOCATOR, udata.change[user_code][0])
        self.fill_field(BL.CHANGE_PHONE_LOCATOR, udata.change[user_code][1])
        self.fill_field(BL.CHANGE_MAIL_LOCATOR, udata.change[user_code][2])


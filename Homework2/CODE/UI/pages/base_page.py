import logging
import pytest
import os
import time

import allure
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CODE.UI.locators.page_locators import BasePageLocators
from CODE.UTILS.decorators import wait

from CODE.UI import user_data as UD

CLICK_RETRY = 3
BASE_TIMEOUT = 30


logger = logging.getLogger('TEST')


class PageNotLoadedException(Exception):
    pass


class BasePage(object):
    url = 'https://target.my.com/'
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        logger.info(f'{self.__class__.__name__} page is opening...')
        assert self.is_opened()

    def is_opened(self):
        def _check_url():
            if self.driver.current_url != self.url:
                raise PageNotLoadedException(
                    f'{self.url} did not opened in {BASE_TIMEOUT} for {self.__class__.__name__}.\n'
                    f'Current url: {self.driver.current_url}.')
            return True

        return wait(_check_url, error=PageNotLoadedException, check=True, timeout=BASE_TIMEOUT, interval=0.1)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 10
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @property
    def action_chains(self):
        return ActionChains(self.driver)



    def scroll_to(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Clicking {locator}')
    def click(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {locator}. Try {i+1} of {CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
                self.scroll_to(element)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    # def multiple_clicks(self, locator, numberofclicks):
    #     for i in range(numberofclicks):
    #         self.click(locator)

    # def move_cursor(self, locator):
    #     self.driver.actions().scroll_to(locator).mouseMove(locator).perform()

    @allure.step('filling {locator}')
    def fill_field(self, locator, data, timeout=None):
        current_field = self.find(locator)
        self.scroll_to(current_field)
        current_field.clear()
        current_field.send_keys(data)

    def upload(self, locator, data, timeout=None):
        current_field = self.find(locator)
        self.scroll_to(current_field)
        current_field.send_keys(data)

    def go_to_login_window(self):
        self.click(self.locators.LOGIN_START_LOCATOR)

    def login_fill(self, user_code):
        self.go_to_login_window()
        self.fill_field(self.locators.LOGIN_MAIL_LOCATOR, UD.login[user_code][0])
        self.fill_field(self.locators.LOGIN_PASSWORD_LOCATOR, UD.login[user_code][1])
        self.click(self.locators.LOGIN_SUBMIT_LOCATOR)




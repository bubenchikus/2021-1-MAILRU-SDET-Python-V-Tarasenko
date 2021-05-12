import allure
import logging
from selenium.webdriver.common.by import By

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

from ui.locators.locators import BaseLocators


CLICK_RETRY = 3
BASE_TIMEOUT = 5


logger = logging.getLogger('test')


class PageNotLoadedException(Exception):
    pass


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver, config):
        self.driver = driver
        self.config = config

        logger.info(f'{self.__class__.__name__} page is opening...')

########################################################################################################################

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

########################################################################################################################

    @allure.step('кликаем на {locator}')
    def click_for_android(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            logger.info(f'Clicking on {locator}. Try {i + 1} of {CLICK_RETRY}...')
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise

    def swipe_up(self, swipetime=200):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    @allure.step('свайпаем до {locator}')
    def swipe_up_to_element(self, locator, max_swipes):
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException(f"Error with {locator}, please check function")
            self.swipe_up()
            already_swiped += 1

    def swipe_element_to_left(self, locator):
        web_element = self.find(locator, 10)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        action. \
            press(x=right_x - 1, y=middle_y). \
            wait(ms=300). \
            move_to(x=left_x + 1, y=middle_y). \
            release(). \
            perform()

    def find_by_text(self, text):
        locator = (By.XPATH, self.locators.RESPONSE.format(text))
        return locator

    def swipe_and_click_by_text(self, text):
        locator = (By.XPATH, self.locators.RESPONSE.format(text))
        self.swipe_element_to_left(locator)
        self.click_for_android(locator)

    def go_back(self, num):
        for i in range(num):
            self.driver.back()

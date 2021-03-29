import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseCase:
    driver = None
    config = None

    def find(self, locator):
        return self.driver.find_element(*locator)

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    def click(self, locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator) and
                                            EC.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, data):
        current_field = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))
        current_field.clear()
        current_field.send_keys(data)

    def close_window(self):
        WebDriverWait(self.driver, 30).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def wait_load(self, locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

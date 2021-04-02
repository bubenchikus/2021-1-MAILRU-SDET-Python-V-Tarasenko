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
        try:
            current_field.send_keys(data)
        except ValueError:
            print('Incorrect data')

    def wait_load(self, locator):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(locator))

    def get_page(self, url):
        if self.driver.current_url != url:
            self.driver.get(url)

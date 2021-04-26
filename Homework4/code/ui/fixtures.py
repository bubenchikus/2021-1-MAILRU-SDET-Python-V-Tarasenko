import os

import allure
import pytest
from appium import webdriver

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.chat_page import ChatPage
from ui.pages.settings_page import SettingsPage

from ui.capability import capability_android


########################################################################################################################

@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)


@pytest.fixture
def main_page(driver, config):
    return MainPage(driver=driver, config=config)


@pytest.fixture
def chat_page(driver, config):
    return ChatPage(driver=driver, config=config)


@pytest.fixture
def settings_page(driver, config):
    return SettingsPage(driver=driver, config=config)


########################################################################################################################


def get_driver(appium_url):
    desired_capabilities = capability_android()
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_capabilities)
    return driver


@pytest.fixture(scope='function')
def driver(config, test_dir):
    appium_url = config['appium']
    driver = get_driver(appium_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def ui_report(driver, request, test_dir, config):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        screenshot_file = os.path.join(test_dir, 'failure.png')
        driver.get_screenshot_as_file(screenshot_file)
        allure.attach.file(screenshot_file, 'failure.png', attachment_type=allure.attachment_type.PNG)

########################################################################################################################


@pytest.fixture(scope='function', autouse=True)
def auto_allow(main_page):
    main_page.allow_access()
    yield


import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', default='http://target.my.com')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    return {'url': url}


@pytest.fixture(scope='function')
def driver(config):
    browser = webdriver.Chrome()
    browser.maximize_window()

    url = config['url']
    browser.get(url)

    yield browser
    browser.quit()

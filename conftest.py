from pytest import fixture
from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser


@fixture(scope='function')
def firefox_browser():
    browser = webdriver.Firefox()
    yield browser


@fixture(scope='function')
def edge_browser():
    browser = webdriver.Edge()
    yield browser

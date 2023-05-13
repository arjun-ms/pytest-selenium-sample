from os import environ

import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver(request):
    brow = "Chrome"

    if (brow == "Chrome"):
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()
    yield browser
from os import environ

import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection


@pytest.fixture(scope='function')
def driver(request):
    execution_mode = environ.get('TEST_EXECUTION_MODE', 'local')  # Environment variable for test execution mode

    if execution_mode == 'local':
        brow = "Chrome"

        if brow == "Chrome":
            browser = webdriver.Chrome()
        else:
            browser = webdriver.Firefox()
    
    elif execution_mode == 'cloud':
        desired_caps = {}

        browser = {
            "platform": "Windows 10",
            "browserName": "chrome",
            "version": "latest"
        }

        desired_caps.update(browser)
        test_name = request.node.name
        build = environ.get('BUILD', "Sample PY Build")
        tunnel_id = environ.get('TUNNEL', False)
        username = environ.get('LT_USERNAME', None)
        access_key = environ.get('LT_ACCESS_KEY', None)

        selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
        desired_caps['build'] = build
        desired_caps['name'] = test_name
        desired_caps['video'] = True
        desired_caps['visual'] = True
        desired_caps['network'] = True
        desired_caps['console'] = True
        caps = {"LT:Options": desired_caps}

        executor = RemoteConnection(selenium_endpoint)
        browser = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=caps
        )

    yield browser

    def fin():
        if execution_mode == 'cloud':
            if request.node.rep_call.failed:
                browser.execute_script("lambda-status=failed")
            else:
                browser.execute_script("lambda-status=passed")
            browser.quit()

    request.addfinalizer(fin)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)
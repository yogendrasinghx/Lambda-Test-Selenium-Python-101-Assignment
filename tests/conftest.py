from os import environ
import pytest
from selenium import webdriver
from selenium.common.exceptions import JavascriptException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from testData.GlobalData import GlobalData


@pytest.fixture(scope='class', params=GlobalData.test_environment)
def driver_init(request):
    desired_caps = {}
    browser = request.param
    desired_caps.update(browser)
    test_name = request.node.name
    build = environ.get('BUILD', "Selenium Python 101")
    tunnel_id = environ.get('TUNNEL', False)
    username = "YOUR_USERNAME"
    access_key = "YOUR_KEY"

    selenium_endpoint = "http://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key)
    desired_caps['build'] = build
    desired_caps['name'] = test_name
    desired_caps['video'] = True
    desired_caps['visual'] = True
    desired_caps['network'] = True
    desired_caps['console'] = True
    caps = {"LT:Options": desired_caps}
    
    executor = RemoteConnection(selenium_endpoint)
    driver = webdriver.Remote(
        command_executor=executor,
        desired_capabilities=caps
    )
    
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


def change_test_status(driver,flag):
    try:
        if flag:
            driver.execute_script('lambda-status=passed')
        else:
            driver.execute_script('lambda-status=failed')
    except JavascriptException:
        pass

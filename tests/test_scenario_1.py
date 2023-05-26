import pytest
from pageObjects.SeleniumPlaygroundPage import SeleniumPlaygroundPage
from pageObjects.SimpleFormDemo import SimpleFormDemo


@pytest.mark.usefixtures("driver_init")
@pytest.mark.timeout(20)
class TestScenario1:
    def test_scenario_1(self, driver_init):
        selenium_playground = SeleniumPlaygroundPage(driver_init)
        selenium_playground.open_playground()
        simple_form_demo = selenium_playground.click_simple_form_demo()
        simple_form_demo.validate_url_contains("simple-form-demo")
        message = "Welcome to LambdaTest"
        simple_form_demo.enter_message(message)
        simple_form_demo.click_get_checked_value()
        simple_form_demo.validate_message_displayed(message)

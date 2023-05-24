from pageObjects.PlayGroundPage import PlayGroundPage
from testData.SimpleFormDemoData import SimpleFormDemoData
from utilities.BaseClass import BaseClass


class TestScenario1(BaseClass):
    def test_scenario_1(self):
        driver = self.driver
        playGroundPage = PlayGroundPage(driver)
        simpleFormDemo = playGroundPage.click_simple_form_demo_link()
        assert "simple-form-demo" in driver.current_url
        message = SimpleFormDemoData.message
        simpleFormDemo.get_message_textbox().send_keys(message)
        simpleFormDemo.get_check_value_button().click()
        assert message == simpleFormDemo.get_show_message().text

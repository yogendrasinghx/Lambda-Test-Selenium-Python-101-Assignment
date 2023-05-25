import time

from selenium.webdriver import ActionChains, Keys

from pageObjects.PlayGroundPage import PlayGroundPage
from utilities.BaseClass import BaseClass


class TestScenario2(BaseClass):
    def test_scenario_2(self):
        driver = self.driver

        playGroundPage = PlayGroundPage(driver)
        dragDropPage = playGroundPage.click_drag_and_drop_slider_link()
        slider = dragDropPage.get_slider_15()
        required_slider_value = 95
        slider_value = int(dragDropPage.get_slider_value().text)
        flag = True
        while flag:
            slider_value = int(dragDropPage.get_slider_value().text)
            if required_slider_value > slider_value:
                slider.send_keys(Keys.ARROW_RIGHT)
            elif required_slider_value < slider_value:
                slider.send_keys(Keys.ARROW_LEFT)
            elif required_slider_value == slider_value:
                flag = False
        assert required_slider_value == slider_value


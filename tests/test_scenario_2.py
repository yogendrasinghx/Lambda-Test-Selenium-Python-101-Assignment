import time

from selenium.webdriver import ActionChains

from pageObjects.PlayGroundPage import PlayGroundPage
from utilities.BaseClass import BaseClass


class TestScenario2(BaseClass):
    def test_scenario_2(self):
        driver = self.driver

        playGroundPage = PlayGroundPage(driver)
        dragDropPage = playGroundPage.click_drag_and_drop_slider_link()
        slider = dragDropPage.get_slider_15()
        action = ActionChains(self.driver)
        slider_value = dragDropPage.get_slider_value()
        '''required_slider_value = 85
        slider_value = int(dragDropPage.get_slider_value().text)
        while slider_value < required_slider_value:
            action.drag_and_drop_by_offset(slider,5,0).perform()
            slider_value = int(dragDropPage.get_slider_value().text)'''

        '''
        # Set the value attribute of the slider using JavaScript
        desired_value = 95
        driver.execute_script("arguments[0].value = arguments[1]", slider, desired_value)

        # Update the output element's value manually
        driver.execute_script("arguments[0].innerHTML = arguments[1]", slider_value, desired_value)'''



        time.sleep(20)
